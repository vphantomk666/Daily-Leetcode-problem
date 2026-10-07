class Solution {
    public String intToRoman(int num) {
        Map<Integer, String> roman = new HashMap<>();

        roman.put(1, "I");
        roman.put(4, "IV");
        roman.put(5, "V");
        roman.put(9, "IX");
        roman.put(10, "X");
        roman.put(40, "XL");
        roman.put(50, "L");
        roman.put(90, "XC");
        roman.put(100, "C");
        roman.put(400, "CD");
        roman.put(500, "D");
        roman.put(900, "CM");
        roman.put(1000, "M");


        int[] values = {
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        };

        String result = "";

        for (int value : values) {
            while (num >= value) {
                result += roman.get(value);
                num -= value;
            }
        }

        return result;
        
    }
}