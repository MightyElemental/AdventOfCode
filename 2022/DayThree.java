package tk.mightyelemental.aoc;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

/**
 * @see <a href="https://adventofcode.com/2022/day/3">https://adventofcode.com/2022/day/3</a>
 * @author MightyElemental
 */
public class DayThree {

	/** List of all rucksacks */
	public static List<String> rucksacks = new ArrayList<>();

	public static void main( String[] args ) {
		// load input
		try (Stream<String> stream = Files.lines(Paths.get("day3_input.txt"), StandardCharsets.UTF_8)) {
			stream.forEach(s -> rucksacks.add(s));
		} catch (IOException e) {
			e.printStackTrace();
		}

		// Part 1
		int prioritySum = 0;
		for (String s : rucksacks) {
			long[] comps = getRucksackCompartments(s);
			prioritySum += getCommonPriority(comps[0], comps[1]);
		}
		System.out.printf("Part 1: %d\n", prioritySum);

		// Part 2
		prioritySum = 0;
		for (int i = 0; i < rucksacks.size(); i += 3) {
			long r1 = compartmentToOneHot(rucksacks.get(i));
			long r2 = compartmentToOneHot(rucksacks.get(i + 1));
			long r3 = compartmentToOneHot(rucksacks.get(i + 2));
			prioritySum += getCommonPriority(r1, r2, r3);
		}
		System.out.printf("Part 2: %d\n", prioritySum);
	}

	/**
	 * Split the rucksack in half and return the one-hot encoding of both halves.
	 * 
	 * @param rucksack the whole rucksack contents
	 * @return The one-hot encodings of both halves
	 */
	public static long[] getRucksackCompartments( String rucksack ) {
		var comp1 = rucksack.substring(0, rucksack.length() / 2);
		var comp2 = rucksack.substring(rucksack.length() / 2, rucksack.length());
		return new long[] { compartmentToOneHot(comp1), compartmentToOneHot(comp2) };
	}

	/**
	 * Generate a one-hot encoded binary string containing the alphabet characters found in the input.<br>
	 * 
	 * <pre>
	 * > Long.toBinaryString(compartmentToOneHot("HelloWorld"));
	 * 1000000000000001000000000000000100100100000011000
	 * </pre>
	 * 
	 * @param contents the characters to encode
	 * @return The one-hot encoding
	 * 
	 */
	public static long compartmentToOneHot( String contents ) {
		long result = 0;
		for (int i = 0; i < contents.length(); i++) {
			char c = contents.charAt(i);
			result |= 1l << (c - (c >= 97 ? 97 : 39));
		}
		return result;
	}

	/**
	 * Finds a character common to all one-hot encodings and returns their priority. This is assuming there is only one
	 * common character, otherwise it will return only the highest priority character.
	 * 
	 * @param comp1 the first encoding to compare
	 * @param comps the collection of multiple encodings to compare to the first and each other
	 * @return The priority of the highest common character
	 */
	public static int getCommonPriority( long comp1, long... comps ) {
		long common = comp1;
		for (long c : comps) common &= c;
		int priority = 0;
		while (priority < 52 && Long.compareUnsigned(common >>>= 1l, 0) > 0) priority++;
		return priority + 1;
	}

}
