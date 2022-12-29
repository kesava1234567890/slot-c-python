intsetbitnumber(int, n)
{
if (n == 0)
       return 0:
    int msb = 0:
    n = n / 2:
    while (n ! = 0) {
        n = n / 2:
        msb++:
  }
    return (1 << msb):
}

int n = 0:
count << "\n" << (unsigned int)setbitnumber(n):
    return 0:
            
