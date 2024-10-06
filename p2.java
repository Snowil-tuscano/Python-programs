import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Callable;
import java.util.concurrent.Future;

class SublistSumTask implements Callable<Integer> {
    private List<Integer> sublist;

    public SublistSumTask(List<Integer> sublist) {
        this.sublist = sublist;
    }

    @Override
    public Integer call() throws Exception {
        int sum = 0;
        for (int num : sublist) {
            sum += num;
        }
        return sum;
    }
}

public class MultiThreadedSum {
    public static void main(String[] args) throws Exception {
        int totalNumbers = 1000000; // size of the list
        int numThreads = 10; // number of threads
        
        List<Integer> largeList = new ArrayList<>();
        Random random = new Random();

        // Fill the list with random integers
        for (int i = 0; i < totalNumbers; i++) {
            largeList.add(random.nextInt(100)); // random integers between 0 and 100
        }

        int sublistSize = totalNumbers / numThreads; // size of each sublist

        // Create a thread pool with a fixed number of threads
        ExecutorService executorService = Executors.newFixedThreadPool(numThreads);
        List<Future<Integer>> futures = new ArrayList<>();

        for (int i = 0; i < numThreads; i++) {
            int start = i * sublistSize;
            int end = (i == numThreads - 1) ? totalNumbers : (i + 1) * sublistSize; // handle the last sublist

            List<Integer> sublist = largeList.subList(start, end);
            SublistSumTask task = new SublistSumTask(sublist);
            Future<Integer> future = executorService.submit(task);
            futures.add(future);
        }

        int overallSum = 0;
        for (Future<Integer> future : futures) {
            overallSum += future.get();
        }

        System.out.println("Overall sum of the list: " + overallSum);

        executorService.shutdown();
    }
}
