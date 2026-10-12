import java.util.*;
class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        int used = 0;
        List<String> s = new ArrayList<>();

        for (String w : words) {
            if (s.isEmpty() || w.length() + used + s.size() <= maxWidth) {
                used += w.length();
                s.add(w);
            } else {
                if (s.size() == 1) {
                    res.add(s.get(0) + " ".repeat(maxWidth - used));
                } else {
                    int totalSpaces = maxWidth - used;
                    int gaps = s.size() - 1;
                    int base = totalSpaces / gaps;
                    int extra = totalSpaces % gaps;

                    StringBuilder line = new StringBuilder();

                    for (int i = 0; i < s.size(); i++) {
                        line.append(s.get(i));

                        if (i < gaps) {
                            int count = base + (i < extra ? 1 : 0);
                            line.append(" ".repeat(count));
                        }
                    }

                    res.add(line.toString());
                }

                used = w.length();
                s = new ArrayList<>();
                s.add(w);
            }
        }

        String last = String.join(" ", s);
        last += " ".repeat(maxWidth - last.length());
        res.add(last);

        return res;
    }
}
