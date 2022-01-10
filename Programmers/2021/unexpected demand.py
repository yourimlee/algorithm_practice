 def filledOrders(order, k):
      fulfilled=0
      if order == 0 or k == 0:
        return 0
      else:
        order.sort()
        for i in range(len(order)):
            left = k-order[i]
            if(left >= 0):
                fulfilled += 1
                k -= order[i]
        return(fulfilled)