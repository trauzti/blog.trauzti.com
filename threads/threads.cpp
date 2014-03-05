#include <thread>
#include <atomic>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define NUM_THREADS 8
#define PER_THREAD 20000000

atomic_ulong sum(0);

void func(int tid) {
  unsigned long int start = tid;
  for (unsigned long int j = start * PER_THREAD + 1; j <= (start+1) * PER_THREAD; j++) {
    sum += j; // atomic operation
  }
}

int main (void) {
  thread *t = new thread[NUM_THREADS];

  for (int i = 0; i < NUM_THREADS; i++)
    t[i] = thread(func, i);
  
  for (int i = 0; i < NUM_THREADS; i++)
    t[i].join();

  unsigned long int n = PER_THREAD * NUM_THREADS;
  printf("sum=%lu vs %lu\n", sum.load(), n * (n+1)  / 2);
  return 0;
}
