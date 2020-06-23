// CS111PA1A2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

//#include "stdafx.h"
#include <opencv2\opencv.hpp>


using namespace std;
using namespace cv;

Mat BoxFilterGray3(Mat I, bool zeroNotMirror);

int main()
{
	string v1pics[6] = { "nature.jpg", "street.jpg", "text.jpg", "kitty.jpg", "berry.jpg", "cartoon.jpg" };
	string v2pics[6] = { "nature2.jpg", "street2.jpg", "text2.jpg", "kitty2.jpg", "berry2.jpg", "cartoon2.jpg" };
	for (int numpics = 0; numpics < 6; numpics++)
	{
		Mat I = imread(v1pics[numpics], CV_LOAD_IMAGE_GRAYSCALE);
		Mat J = BoxFilterGray3(I, true);
		imwrite(v2pics[numpics], J);
	}
	return 0;
}

Mat BoxFilterGray3(Mat I, bool zeroNotMirror) {
	Mat J(I.rows, I.cols, CV_8UC1);
	for (int i = 0; i < I.rows; i++) {
		for (int j = 0; j < I.cols; j++) {
			int total = int(I.at<uchar>(i,j));
			if (zeroNotMirror) { //zero padding
				if (i != 0) {
					total += int(I.at<uchar>(i - 1, j));
					if (j != 0) {
						total += int(I.at<uchar>(i - 1, j - 1));
					}
					if (j != I.cols - 1) {
						total += int(I.at<uchar>(i - 1, j + 1));
					}
				}
				if (i != I.rows-1) {
					total += int(I.at<uchar>(i + 1, j));
					if (j != 0) {
						total += int(I.at<uchar>(i + 1, j - 1));
					}
					if (j != I.cols - 1) {
						total += int(I.at<uchar>(i + 1, j + 1));
					}
				}
				if (j != 0) {total += int(I.at<uchar>(i, j - 1));}
				if (j != I.cols - 1) { total += int(I.at<uchar>(i, j + 1)); }
			}
			else { //Mirror
				int il = i - 1;
				if (il < 0) { il = 0; }
				int ir = i + 1;
				if (ir > I.rows - 1) { ir = I.rows - 1; }
				int ju = j - 1;
				if (ju < 0) { ju = 0; }
				int jd = j + 1;
				if (jd > I.cols - 1) { jd = I.cols - 1; }
				total += int(I.at<uchar>(il, ju));
				total += int(I.at<uchar>(il, j));
				total += int(I.at<uchar>(il, jd));
				total += int(I.at<uchar>(i, ju));
				total += int(I.at<uchar>(i, jd));
				total += int(I.at<uchar>(ir, ju));
				total += int(I.at<uchar>(ir, j));
				total += int(I.at<uchar>(ir, jd));
			}

			J.at<uchar>(i, j) = uchar(total / 9);
		}
	}
	return J;
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
