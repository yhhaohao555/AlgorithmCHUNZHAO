class Solution {
    public int nthUglyNumber(int n) {
        PriorityQueue<Long> heap = new PriorityQueue<Long>();
        int[] cut = new int[]{2, 3, 5};
        heap.add(1L);
        int count = 0;
        long ans = 0;
        while (count < n) {
            ans = heap.poll();
            for (int e: cut) {
                if (!heap.contains(ans * e)) {
                    heap.add(ans * e);
                }
            }
            count++;
        }
        return (int) ans;
    }
}