#include <stdio.h>
#include <stdlib.h>
#include <time.h> // for clock_gettime

int main(void) {
  unsigned long int i, j;
  struct timespec t1, t2;
  int secs, nsecs;
  clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &t1);
  for (i = 0; i < 1000000000; i++) {
    j += i*i;
  }
  clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &t2);
  double diff = (t2.tv_sec - t1.tv_sec) + (t2.tv_nsec - t1.tv_nsec) / 1E9;
  printf("%lfs\n", diff);
  return 0;
}
