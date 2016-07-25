Project contains openCV built in samples.

To run some specific sample go to main.cpp
1) Include desired sample
2) Define its name as sampleName

Example for Watershed sample:
#include "cppSamples\watershed.h"	// include sample header here
#define sampleName watershed		// set sample name her

Most samples require input parameters
To set them up:
1) Open OpenCvPlaygound project properties (right click -> Properties in the end of context menu)
2) Go to Configuration Properties -> Debugging -> set Command Arguments property
3) Apply/OK
