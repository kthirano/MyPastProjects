// CS111PA1A2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

//#include "stdafx.h"
#include <opencv2\opencv.hpp>
#include <math.h>


using namespace std;
using namespace cv;
/*
Mat CreateGaussianFilter();
Mat ApplyFilter(Mat input, Mat filter);
Mat Reduce(Mat input);
*/
void DFTShift(Mat& I);
void DFT(Mat Input, Mat& Real, Mat& Imag);


int main()
{
	string v1pics[5] = { "I1.png", "I2.png", "I3.png", "I4.png", "I5.png"};
	string v2pics[5] = { "mag1.png", "mag2.png", "mag3.png", "mag4.png", "mag5.png" };
	//const double pi = 3.141592653589793;
	for (int numpics = 0; numpics < 5; numpics++) {
		Mat I = imread(v1pics[numpics], CV_8UC1);
		Mat real(I.rows, I.cols, CV_32FC1);
		Mat imag(I.rows, I.cols, CV_32FC1);
		Mat magn(I.rows, I.cols, CV_32FC1);
		Mat phas(I.rows, I.cols, CV_32FC1);
		Mat post(I.rows, I.cols, CV_32FC1);
		Mat output(I.rows, I.cols, CV_8UC1);
		DFT(I, real, imag);
		magnitude(real, imag, magn);
		phase(real, imag, phas);
		DFTShift(magn);
		DFTShift(phas);
		normalize(magn, post, 0, 255, NORM_MINMAX);
		post.convertTo(output, CV_8UC1);
		imwrite(v2pics[numpics], output);
	}

		//Mat I = imread(v1pics[numpics], CV_8UC1);
		//Mat J2(I.rows, I.cols, CV_8UC1); //CV_8UC1
		/*
		
		Mat J(512, 512, CV_32FC1); //CV_8UC1
		Mat I(512, 512, CV_32FC1);
		Mat K(512, 512, CV_8UC1);
		for (int i = 0; i < 512; i++) {
			for (int j = 0; j < 512; j++) {
				J.at<float>(i, j) = 1 + sin(0.1 * pi * i);
			}
		}
		normalize(J, I, 0, 255, NORM_MINMAX);
		I.convertTo(K, CV_8UC1);
		imwrite(v1pics[0], K);
		for (int i = 0; i < 512; i++) {
			for (int j = 0; j < 512; j++) {
				J.at<float>(i, j) = 1 + cos(cos(0.2 * pi * j));
			}
		}
		normalize(J, I, 0, 255, NORM_MINMAX);
		I.convertTo(K, CV_8UC1);
		imwrite(v1pics[1], K);
		for (int i = 0; i < 512; i++) {
			for (int j = 0; j < 512; j++) {
				J.at<float>(i, j) = 1 + cos(cos(0.4 * pi * i));
			}
		}
		normalize(J, I, 0, 255, NORM_MINMAX);
		I.convertTo(K, CV_8UC1);
		imwrite(v1pics[2], K);
		for (int i = 0; i < 512; i++) {
			for (int j = 0; j < 512; j++) {
				J.at<float>(i, j) = 1 + sin(0.15 * pi * sqrt(i * i + j * j));
			}
		}
		normalize(J, I, 0, 255, NORM_MINMAX);
		I.convertTo(K, CV_8UC1);
		imwrite(v1pics[3], K);
		for (int i = 0; i < 512; i++) {
			for (int j = 0; j < 512; j++) {
				J.at<float>(i, j) = 1 + sin(0.35 * pi * sqrt(i * i + j * j));
			}
		}
		normalize(J, I, 0, 255, NORM_MINMAX);
		I.convertTo(K, CV_8UC1);
		imwrite(v1pics[4], K);
		*/
	return 0;
}

void DFTShift(Mat& I) {

	int cx = I.cols / 2;
	int cy = I.rows / 2;

	// Define quadrants
	Mat q0(I, Rect(0, 0, cx, cy));   // Top-Left 
	Mat q1(I, Rect(cx, 0, cx, cy));  // Top-Right
	Mat q2(I, Rect(0, cy, cx, cy));  // Bottom-Left
	Mat q3(I, Rect(cx, cy, cx, cy)); // Bottom-Right

	Mat temp;                           // swap quadrants (q0 and q2)
	q0.copyTo(temp);
	q3.copyTo(q0);
	temp.copyTo(q3);

	q1.copyTo(temp);                    // swap quadrant (q1 and q3)
	q2.copyTo(q1);
	temp.copyTo(q2);

}

void DFT(Mat Input, Mat& Real, Mat& Imag) {
	// I:    [In]   Gray Image
	// Real: [Out]  Real part of DFT
	// Imag: [Out]  Imaginary part of DFT

	// Converting input image to type float 
	Mat I, II;
	Input.convertTo(I, CV_32FC1);

	// Creating two channel input to represent
	Mat channels[] = { I, Mat::zeros(I.size(), CV_32FC1) };
	merge(channels, 2, II);

	// Calculate DFT
	dft(II, II);

	// Returning results
	split(II, channels);
	Real = channels[0];
	Imag = channels[1];
}
