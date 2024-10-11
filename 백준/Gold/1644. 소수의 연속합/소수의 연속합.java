import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static boolean[] primeNum(int x) {
        boolean[] isPrime=new boolean[x+1];
        Arrays.fill(isPrime, true);
        isPrime[0]=false;
        isPrime[1]=false;
        for (int i = 2; i * i <= x; i++) {
            if (isPrime[i]) {
                for (int j = i*i; j <= x; j += i) {
                    isPrime[j]=false;
                }
            }
        }
        return isPrime;
    }

    public static void main(String[] args) throws IOException {
        ArrayList<Integer> primeArr=new ArrayList<>();
        boolean [] isPrime=primeNum(4000000);
        for (int i = 2; i < isPrime.length; i++) {
            if (isPrime[i]) {
                primeArr.add(i);
            }
        }
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        int start=0;
        int end=0;
        int count=0;
        int primeSum= primeArr.get(start);
        while (end< primeArr.size()) {
            if (primeSum>N) {
                primeSum-=primeArr.get(start);
                start++;
            } else if (primeSum<N) {
                end++;
                if (end<primeArr.size()) {
                    primeSum += primeArr.get(end);
                }
            } else {
                count++;
                end++;
                if (end<primeArr.size()) {
                    primeSum+=primeArr.get(end);
                }
            }
        }
        System.out.println(count);
    }
}
