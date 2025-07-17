print("Select any two prefered subjects : \n1.Maths\n2.Physics\n3.Biology\n4.Programming\n5.Circuits\n6.Electronics\n7.Statistics\n8.AI Concepts\n9.Chemistry\n")
sub1=int(input("Enter your First Prefered Subject Number : "))
sub2=int(input("Enter your Second Prefered Subject Number : "))
if (sub1==1 and sub2==2) or (sub1==2 and sub2==1) :
	print("\nCareer Suggested - Mechanical Engineering\n")
elif (sub1==1 and sub2==4) or (sub1==4 and sub2==1)  :
	print("\nCareer Suggested - Computer Engineering\n")
elif (sub1==3 and sub2==9) or (sub1==9 and sub2==3) :
	print("\nCareer Suggested - Biotechnology \n")
elif (sub1==1 and sub2==5) or (sub1==5 and sub2==1) :
	print("\nCareer Suggested - Electronics Engineering\n")
elif (sub1==4 and sub2==7) or (sub1==7 and sub2==4) :
	print("\nCareer Suggested - Artificial Intelligence and Data Science\n")
elif (sub1==4 and sub2==8) or (sub1==8 and sub2==4) :
	print("\nCareer Suggested - Artificial Intelligence and Machine Learning Engineering\n")

