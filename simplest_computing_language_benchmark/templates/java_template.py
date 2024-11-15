JAVA_CODE = """
public class Benchmarks {
    public static void arraySum() {
        int[] arr = new int[1000000];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        }
        long sum = 0;
        for (int i : arr) {
            sum += i * 2;
        }
    }

    public static void stringConcat() {
        // Test 1: String building with StringBuilder
        StringBuilder sb1 = new StringBuilder();
        for (int i = 0; i < 10000; i++) {
            sb1.append(i).append("hello");
        }
        String result1 = sb1.toString();
        
        // Test 2: String splitting and processing
        String text = "hello,world,this,is,a,test".repeat(1000);
        String[] words = text.split(",");
        StringBuilder sb2 = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            if (i > 0) sb2.append(",");
            sb2.append(words[i].toUpperCase());
        }
        String result2 = sb2.toString();
        
        // Test 3: String replacements
        String template = "The quick brown fox".repeat(100);
        String result3 = template.replace("quick", "slow")
                              .replace("brown", "red")
                              .replace("fox", "dog");
        
        String finalResult = result1 + result2 + result3;
    }

    public static void mathOps() {
        double sum = 0;
        for (int i = 0; i < 10000; i++) {
            sum += Math.sqrt(i) + Math.sin(i);
        }
    }

    public static void main(String[] args) {
        long startTime, endTime;
        
        // Warm-up
        for (int i = 0; i < 10; i++) {
            arraySum();
            stringConcat();
            mathOps();
        }

        // Actual benchmarks
        double[] arrayTimes = new double[1000];
        double[] stringTimes = new double[1000];
        double[] mathTimes = new double[1000];

        for (int i = 0; i < 1000; i++) {
            startTime = System.nanoTime();
            arraySum();
            endTime = System.nanoTime();
            arrayTimes[i] = (endTime - startTime) / 1e9;

            startTime = System.nanoTime();
            stringConcat();
            endTime = System.nanoTime();
            stringTimes[i] = (endTime - startTime) / 1e9;

            startTime = System.nanoTime();
            mathOps();
            endTime = System.nanoTime();
            mathTimes[i] = (endTime - startTime) / 1e9;
        }

        // Output median results as JSON
        System.out.println("{");
        System.out.printf("\\"java_array_sum\\": %f,%n", median(arrayTimes));
        System.out.printf("\\"java_string_concat\\": %f,%n", median(stringTimes));
        System.out.printf("\\"java_math\\": %f%n", median(mathTimes));
        System.out.println("}");
    }

    private static double median(double[] arr) {
        java.util.Arrays.sort(arr);
        int middle = arr.length / 2;
        if (arr.length % 2 == 0) {
            return (arr[middle-1] + arr[middle]) / 2.0;
        }
        return arr[middle];
    }
}
"""
