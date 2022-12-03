package tk.mightyelemental.aoc;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class DayThree {

	public static List<String> rucksacks = new ArrayList<>();

	public static void main( String[] args ) {
		// load input
		try (Stream<String> stream = Files.lines(Paths.get("day3_input.txt"), StandardCharsets.UTF_8)) {
			stream.forEach(s -> rucksacks.add(s));
		} catch (IOException e) {
			e.printStackTrace();
		}

		// part 1
		int prioritySum = 0;
		for (String s : rucksacks) {
			long[] comps = getRucksackCompartments(s);
			prioritySum += getCommonPriority(comps[0], comps[1]);
		}
		System.out.printf("Part 1: %d\n", prioritySum);

		// part 2
		prioritySum = 0;
		for (int i = 0; i < rucksacks.size(); i += 3) {
			long r1 = compartmentToOneHot(rucksacks.get(i));
			long r2 = compartmentToOneHot(rucksacks.get(i + 1));
			long r3 = compartmentToOneHot(rucksacks.get(i + 2));
			prioritySum += getCommonPriority(r1, r2, r3);
		}
		System.out.printf("Part 2: %d\n", prioritySum);
	}

	public static long[] getRucksackCompartments( String rucksack ) {
		var comp1 = rucksack.substring(0, rucksack.length() / 2);
		var comp2 = rucksack.substring(rucksack.length() / 2, rucksack.length());
		return new long[] { compartmentToOneHot(comp1), compartmentToOneHot(comp2) };
	}

	public static long compartmentToOneHot( String contents ) {
		long result = 0;
		for (int i = 0; i < contents.length(); i++) {
			char c = contents.charAt(i);
			result |= 1l << (c - (c >= 97 ? 97 : 39));
		}
		return result;
	}

	public static int getCommonPriority( long comp1, long... comps ) {
		long common = comp1;
		for (long c : comps) common &= c;
		int priority = 0;
		while (priority < 52 && Long.compareUnsigned(common >>>= 1l, 0) > 0) priority++;
		return priority + 1;
	}

}
