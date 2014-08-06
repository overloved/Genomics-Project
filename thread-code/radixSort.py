def sort( aList, x ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for i in aList:
      tmp = i[x] / placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX
  return aList




# l = [(200, 111), (101, 123), (130, 234), (299, 9)]
# print radixsort(l, 0)
# print radixsort(l, 1)
