import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// 첫째 줄에 주어지는 수의 개수
		int length = Integer.parseInt(br.readLine()); 

		// N개의 수 입력
		int[] input_nums = new int[length];
		for (int i = 0; i < length; i++) {
			input_nums[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(input_nums);
		
		for (int i = 0; i < length; i++) {
			bw.write(input_nums[i] + "\n");
		}
		
		bw.flush();
		bw.close();
		
	}
}