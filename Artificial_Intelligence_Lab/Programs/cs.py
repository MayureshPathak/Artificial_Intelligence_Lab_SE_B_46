print("Select any two prefered subjects : \n1.Maths\n2.Physics\n3.Biology\n4.Programming\n5.Circuits\n6.Electronics\n7.Statistics\n8.AI Concepts\n9.Chemistry\n")
sub1=str(input("Enter your First Prefered Subject : ")).lower()
sub2=str(input("Enter your Second Prefered Subject : ")).lower()
if ((sub1=="maths" and sub2=="physics") or (sub1=="physics" and sub2=="maths")) :
	print("\nCareer Suggested - Mechanical Engineering\n")
elif ((sub1=="maths" and sub2=="programming") or (sub1=="programming" and sub2=="maths") ) :
	print("\nCareer Suggested - Computer Engineering\n")
elif ((sub1=="biology" and sub2=="chemistry") or (sub1=="chemistry" and sub2=="biology")) :
	print("\nCareer Suggested - Biotechnology \n")
elif (sub1=="maths" and sub2=="circuits") or (sub1=="circuits" and sub2=="maths") :
	print("\nCareer Suggested - electronics Engineering\n")
elif (sub1=="programming" and sub2=="statistics") or (sub1=="statistics" and sub2=="programming") :
	print("\nCareer Suggested - Artificial Intelligence and Data Science\n")
elif (sub1=="programming" and sub2=="ai concepts") or (sub1=="ai concepts" and sub2=="programming") :
	print("\nCareer Suggested - Artificial Intelligence and Machine Learning Engineering\n")

