import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        List<String> canSayWord = Arrays.asList("aya", "ye", "woo", "ma");
        for (int i = 0; i < babbling.length; i++) {
            for (int j = 0; j < 4; j++) {
                if (babbling[i].contains(canSayWord.get(j))) {
                    babbling[i] = babbling[i].replace(canSayWord.get(j), "/");
                }
                else continue;
            }
            
            if (babbling[i].matches("[^a-z]*$")) {
                answer += 1;
            }
        }
        return answer;
    }
}