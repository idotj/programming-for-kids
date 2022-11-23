#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  int len;
  int *data;
} list;

// take a list of numbers
// and return an average
// floored, e.g:
//   [1,2]
// returns:
//   1
int avg(list x) {
  int sum = 0;
  for (int i = 0; i < x.len; i++) {
    sum += x.data[i];
  }

  return sum/x.len;
}

int main(void) {
  list x = {
    .len = 10,
    .data = malloc(x.len*4),
  };

  int n = 0;
  x.data[n++] = 1;
  x.data[n++] = 1;
  x.data[n++] = 2;
  x.data[n++] = 3;
  x.data[n++] = 3;
  x.data[n++] = 4;
  x.data[n++] = 1;
  x.data[n++] = 2;
  x.data[n++] = 7;
  x.data[n++] = 1;

  
  printf("%d\n", avg(x));
}
