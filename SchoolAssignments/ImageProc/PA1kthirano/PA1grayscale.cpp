// CS111PA1A2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

//#include "stdafx.h"
#include <opencv2\opencv.hpp>


using namespace std;
using namespace cv;
int main()
{
	string v1pics[6] = { "nature.jpg", "street.jpg", "text.jpg", "kitty.jpg", "berry.jpg", "cartoon.jpg" };
	string v2pics[6] = { "nature2.jpg", "street2.jpg", "text2.jpg", "kitty2.jpg", "berry2.jpg", "cartoon2.jpg" };
	for (int numpics = 0; numpics < 6; numpics++)
	{
		Mat I = imread(v1pics[numpics], CV_LOAD_IMAGE_COLOR);
		Mat J(I.rows, I.cols, CV_8UC1);
		for (int i = 0; i < I.rows; i++) {
			for (int j = 0; j < I.cols; j++) {
				Vec3b pixel = I.at<Vec3b>(i, j);
				int b = pixel[0];
				int g = pixel[1];
				int r = pixel[2];
				J.at<uchar>(i, j) = uchar(0.114*b + 0.5870*g + 0.2990*r);
			}
		}
		imwrite(v2pics[numpics], J);
	}
	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
