import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class day3 {

    public static void main(String[] s) throws IOException {
        System.out.println(parseInput("examples/example3.txt"));
        String instructions = parseInput("inputs/input3.txt");
        System.out.println(p1(instructions));
        System.out.println(p2(instructions));
    }



    private static int p1(String instructions) {
            Pattern mul = Pattern.compile("mul\\((\\d{1,3},\\d{1,3})\\)");
            Matcher matcher = mul.matcher(instructions);
            int total = 0;
            while(matcher.find()){
                total += Arrays.stream(matcher.group(1).split(","))
                        .mapToInt(Integer::parseInt)
                        .reduce(1, (a, b) -> a * b);
            }
            return total;
    }

    private static int p2(String instructions) {
        Pattern mul = Pattern.compile("mul\\((\\d{1,3},\\d{1,3})\\)|do\\(\\)|don't\\(\\)");
        Matcher matcher = mul.matcher(instructions);
        int total = 0;
        Boolean counting = true;
        while(matcher.find()){
            if (matcher.group().equals("do()")){
                counting = true;
            } else if(matcher.group().equals("don't()")){
                counting = false;
            } else {
               if (counting){
                   total += Arrays.stream(matcher.group(1).split(","))
                           .mapToInt(Integer::parseInt)
                           .reduce(1, (a, b) -> a * b);
               }
            }

        }
        return total;
    }

    private static String parseInput(String inputFileName) throws IOException {
        return Files.readString(Path.of(inputFileName));

    }

}
