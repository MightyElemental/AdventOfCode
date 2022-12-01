import System.IO ()
import Control.Monad ()
import Data.List.Split (splitOn)
import Data.List (sort)

-- I forgot how much I hate this language sometimes

main :: IO ()
main = do
        contents <- readFile "day1_input.txt"
        print "task 1"
        print . take 1 . sortedList . lines $ contents
        print "task 2"
        print . sum . take 3 . sortedList . lines $ contents

group :: [String] -> [[String]]
group = splitOn [""]

sumGroup :: [[String]] -> [Int]
sumGroup xs = [sum (map toInt x) | x <- xs]
        where toInt l = read l :: Int

sortedList :: [String] -> [Int]
sortedList = reverse . sort . sumGroup . group