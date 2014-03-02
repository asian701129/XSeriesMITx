def bisectionSearch(mmin,mmax,findthis):
    center = mmax/2
    guess = center
    successflag = 0
    print ('We are searching for your number ' + str(findthis) + ' within the range ' + str(mmin) + ' to ' + str(mmax))
    while successflag == 0:
        
   	
   	switch = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
   	
   	if switch == 'c':
  		break
   	elif switch == 'h':
  		mmax = center
  		center = mmin + (mmax - mmin) / 2
   	elif switch == 'l':
  		mmin = center
  		center = mmin + (mmax - mmin) / 2
   	else:
  		print 'Sorry, I did not understand your input.'
   	guess = center
   	
    print "Game over. Your secret number was:",
    print guess
