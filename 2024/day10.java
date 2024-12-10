import java.awt.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.List;

public class day10 {


    public static void main(String[] s) throws IOException {
        Map<Point, Integer> landMap = parseFile("inputs/input10.txt");
        List<Point> heads = getHeads(landMap);

        int resP1 = p1(landMap, heads);
        System.out.println(resP1);
        int resP2 = p2(landMap, heads);
        System.out.println(resP2);
    }

    private static Integer p1(Map<Point, Integer> landMap,
                              List<Point> heads){
        int tot = 0;
        for(Point head : heads){
            tot += hike(landMap, head, 9, new ArrayList<>() );
        }
        return tot;


    }
    private static Integer p2(Map<Point, Integer> landMap,
                              List<Point> heads){
        int tot = 0;
        for(Point head : heads){
            tot += hike(landMap, head, 9, null);
        }
        return tot;


    }
    private static Integer hike(Map<Point, Integer> landMap,
                                Point pos, Integer target,
                                List<Point> visited) {
        Integer tot = 0;
        int[][] dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        if (visited != null && visited.contains(pos)) {
            return 0;
        }

        if (visited != null) {
            visited.add(pos);
        }
        Integer currVal = landMap.get(pos);
        if (Objects.equals(currVal, target)) {
            return 1;
        }

        for (int[] dir: dirs){
            Point next = new Point(pos.x+dir[0], pos.y+dir[1]);
            if (landMap.get(next) == null || landMap.get(next) - currVal != 1){
                continue;
            }
            tot += hike(landMap, next, target, visited);
        }
        return tot;

    }

    private static Point getBounds(Map<Point, Integer> allPoints) {
        return allPoints.keySet().stream()
                .max(Comparator.comparing(p -> p.x + p.y))
                .orElse(null);
    }

    private static List<Point> getHeads(Map<Point, Integer> allPoints) {
        List<Point> heads = new ArrayList<>();
        for (Map.Entry<Point, Integer> e : allPoints.entrySet()) {
            Integer v = e.getValue();
            if (v != 0) {
                continue;
            }
            Point p = e.getKey();
            heads.add(p);
        }
        return heads;

    }

    private static Map<Point, Integer> parseFile(String filePath) throws IOException {
        Map<Point, Integer> map = new HashMap<>();

        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;
        int row = 0;

        while ((line = reader.readLine()) != null) {
            for (int col = 0; col < line.length(); col++) {
                int val = line.charAt(col) - '0';
                Point key = new Point(row, col);
                map.put(key, val);
            }
            row++;
        }

        reader.close();
        return map;
    }
}
