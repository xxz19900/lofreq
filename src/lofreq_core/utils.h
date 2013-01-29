#include <limits.h>

int file_exists(char *fname);
int ae_load_file_to_memory(const char *filename, char **result);
int int_cmp(const void *a, const void *b);
int argmax_d(const double *arr, const int n);

typedef struct {
     unsigned long int n; /* number of elements stored */
     int *data; /* actual array of data */

     size_t grow_by_size; /* if needed grow array by this value. will double previous size if <=1 */
     size_t alloced; /* actually allocated size for data */
} int_varray_t;

void int_varray_add_value(int_varray_t *a, const int value);
void int_varray_free(int_varray_t *a);
void int_varray_init(int_varray_t *a, 
                     const size_t grow_by_size);