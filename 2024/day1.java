import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

import static java.util.Collections.sort;

public class day1 {

    private static Integer p1(List<Integer> l1, List<Integer> l2){
        return IntStream.range(0, l1.size()).map(i -> Math.abs(l1.get(i)-l2.get(i))).sum();
    }

    private static Integer p2(List<Integer> l1, List<Integer> l2){
        return l1.stream().mapToInt(num -> num * Collections.frequency(l2, num)).sum();
    }

    public static void main(String[] s) {
        List<Integer> firstList = new ArrayList<>();
        List<Integer> secondList = new ArrayList<>();


        {
            try {
                List<String> lines = Files.readAllLines(Path.of("examples/example1.txt"));
                for (String line : lines) {
                    String[] parts = line.trim().split("\\s+"); // Split by whitespace
                    if (parts.length == 2) {
                        firstList.add(Integer.parseInt(parts[0]));
                        secondList.add(Integer.parseInt(parts[1]));
                    }
                }

                sort(firstList);
                sort(secondList);

                System.out.println(p1(firstList, secondList));
                System.out.println(p2(firstList, secondList));

            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
