							AUTOMATIC BUG TRIAGING A MACHINE LEARNING APPROACH


-== Version 1.0 ==-
-== 6th April 2015 ==-

-==	System Requirements ==-

Operating System: Ubuntu 13.04 or Fedora 19 or Equivalent *Nix
CPU: Intel Core i3 or higher
Memory: 4GB of RAM or higher
Hard Drive: 500 MB freespace 
Media: 8x CD ROM or higher
Graphics Hardware: OpenGL compatible Graphics Card

-== Package Contents ==-

The CD Package consists of 
• Final Report of the project.
• The requisite program files.
• Dataset.
• The references document.
• This ReadMe.txt.

The requisite program files comprises of
• The JSON and XML file
• The excutable Python script

-== Software Pre-Requisites ==-

The program requires the following packages to be available as part of the runtime environment
to function properly.

	1. There are certain standard packages which are needed by the program to run. These
	include python compilers and several more packages

	For Ubuntu, open a terminal and run the following commands

	sudo apt-get install build-essential
	sudo apt-get install python

	For Fedora, open a terminal and run the following commands

	sudo yum groupinstall "Development tools"
	sudo yum install python

	2. Necessary packages required (NLTK, pandas, Textblob, pip) are to be installed

	For Ubuntu, open a terminal and run the following commands,

	sudo apt-get install pip
	sudo pip install nltk
	sudo pip install pandas
	sudo pip install textblob 

	For Fedora, open a terminal and run the follwing commands,

	sudo yum install pip
	sudo pip install nltk
	sudo pip install pandas
	sudo pip install textblob

-== Running the program ==-

Follow the steps to run the program

	1. Copy the folder "Dataset" and "Program" from the CD to your local hard drive under the same directory.

	2. Open a terminal window and navigate to "Program" folder on your hard drive

	3. When you run the program for the first time, open a new terminal and run the following commands

		python test1.py      		//This is to obtain the dataset into proper input format required to train classifier.
		python stop_stem.py  		//This is to remove stop words and stem the input text file.
		python data_save.py  		//This is to convert the text file into a feature-vector format as input to classifier.
		python review2.py    		//This is to train the classifier and dump the result in pickle. Input from user is obtained to predict the 							  accurate developer to whom the bug will be accurately fixed.
		python toss_data    		// This is to obtain the tossing history of developer from the dataset.
		python toss_data_extraction.py  //This is to predict the 10 highest probable tosses done by a developer.

	4. From the initial run of the program, the following text files and pkl files will be created.
		output_dev      //Input to stop_stem.py. Output from test1.py to obtain the text file.
		output_devnew   //Input to data_save.py. Ouput from stop_stem.py after stop-word removal.
		data_new.pkl    // Feature vector pair obtained after data_save.py.
		trained_data.pkl //Trained classifier after review2.py
		output_toss	 //Output obtained after toss_graph.py where the developer and the component in which he fixed the bugs are stored.
		toss_data	 // Ouput from toss_data_extraction.py where the tosses of a developer is kept track of.

-== Change Log ==-

	Version 1.0 - The first version of automatic bug triaging using machine learning algorithm.

-== Contact Information ==-

For any futher details regarding Automatic Bug Triaging to developers, you can reach the developers at the following
email addresses:
	
	Saagarikha S  - sags.srini@gmail.com
	Susindaran E  - susindaran94@gmail.com
	Venugopal C G - gopalcg123@gmail.com
