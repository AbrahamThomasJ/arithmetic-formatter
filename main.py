from arithmetic_arranger import arithmetic_arranger

def run():

   print( arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]) )
   print('******   ******   ' * 2)
   print( arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True) )


if __name__ == "__main__":
   run()