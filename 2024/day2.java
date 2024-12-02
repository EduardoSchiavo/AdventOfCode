import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class day2 {

    public static void main(String[] s) {
        List<List<Integer>> input = parseInput();
        System.out.println(p1(input));
        System.out.println(p2(input));
    }

    private static Integer p1(List<List<Integer>> records){
        return records.stream().mapToInt(record -> isSafe(record) ? 1 : 0).sum();
    }

    private static Integer p2(List<List<Integer>> records){
        return records.stream().mapToInt(record -> isSafeWithDampener(record) ? 1 : 0).sum();
    }

    private static boolean isSafe(List<Integer> record){
        int sign = (int) Math.signum(record.get(1)-record.get(0));
        for (int i = 1; i < record.size(); i++){
            int diff = Math.abs(record.get(i)-record.get(i-1));
            int currSign = (int) Math.signum(record.get(i)-record.get(i-1));
            if (diff > 3 || diff < 1 || currSign != sign) {
                return false;
            }
        }
        return true;
    }

    private static boolean isSafeWithDampener(List<Integer> record){
        if (isSafe(record)){
            return true;
        }
        for (int i = 0; i < record.size(); i++){
            List<Integer> copy = new ArrayList<>(record);
            copy.remove(i);
            if (isSafe(copy)){
                return true;
            }
        }
        return false;
    }

    private static List<List<Integer>> parseInput() {
        List<List<Integer>> inp = new ArrayList<>();

        try {
            List<String> lines = Files.readAllLines(Path.of("inputs/input2.txt"));
            for (int i = 0; i < lines.size(); i++){
                List<Integer> numbers = Arrays.stream(lines.get(i).split("\\s+")) // Split by whitespace
                        .map(Integer::parseInt)
                        .toList();
                inp.add(numbers);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return inp;
    }
}

