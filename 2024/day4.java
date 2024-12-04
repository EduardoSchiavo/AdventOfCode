import java.awt.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.net.StandardSocketOptions;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class day4 {


    public static void main(String[] s) throws IOException {
        Map<Point, Character> wordSearch = parseFile("inputs/input4.txt");
        System.out.println(part1(wordSearch));
        System.out.println(part2(wordSearch));
    }

    private static int part1(Map<Point, Character> ws) {
        int[][] directionOffsets = {
                {1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}
        };
        int tot = 0;
        for (Map.Entry<Point, Character> entry : ws.entrySet()) {
            if (entry.getValue() == 'X') {
                for (int[] directionOffset : directionOffsets) {
                    if (isXmas(ws, entry.getKey(), directionOffset)) {
                        tot += 1;
                    }
                }
            }
        }
        return tot;
    }

    private static int part2(Map<Point, Character> ws){
        int tot = 0;
        for (Map.Entry<Point, Character> entry : ws.entrySet()) {
            if (entry.getValue() == 'A') {
                if (isCross(ws, entry.getKey())){
                tot+=1;
                }
            }
            }
        return tot;
    }

    private static Boolean isCross(Map<Point, Character> ws, Point pos) {
        int[][] cornerOffsets = {
                {1, 1}, {-1, -1}, {1, -1}, {-1, 1}
        };
        Set<Character> validChars = Set.of('M', 'S');
        Point[] corners = new Point[4];
        for (int i = 0; i < corners.length; i++) {
            corners[i] = new Point(pos.x + cornerOffsets[i][0], pos.y + cornerOffsets[i][1]);
        }
        if (ws.get(corners[0]) == ws.get(corners[1]) || (ws.get(corners[2]) == ws.get(corners[3])
        )) {
            return false;
        }
        for (Point corner : corners) {
            if (ws.get(corner) == null || !validChars.contains(ws.get(corner))) {
                return false;
            }
        }
        return true;

    }

    private static Boolean isXmas(Map ws, Point pos, int[] dir) {
        String mas = "MAS";
        StringBuilder builder = new StringBuilder();
        for (int i = 1; i < 4; i++) {
            Point next = new Point(pos.x + i * dir[0], pos.y + i * dir[1]);
            builder.append(ws.get(next));
        }
        String word = builder.toString();

        return word.equals(mas);

    }

    private static Map<Point, Character> parseFile(String filePath) throws IOException {
        Map<Point, Character> map = new HashMap<>();

        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;
        int row = 0;

        while ((line = reader.readLine()) != null) {
            for (int col = 0; col < line.length(); col++) {
                char letter = line.charAt(col);
                // Using "row,col" as a string representation of coordinates
                Point key = new Point(row, col);
                map.put(key, letter);
            }
            row++;
        }

        reader.close();
        return map;
    }
}

