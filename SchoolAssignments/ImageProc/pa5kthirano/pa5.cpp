Mat Resize(Mat I, float s) {
	int orig_x = I.cols;
	int orig_y = I.rows;
	int tar_x = orig_x * s;
	int tar_y = orig_y * s;
	// Query points
	Mat X(tar_y, tar_x, CV_32FC1);
	Mat Y(tar_y, tar_x, CV_32FC1);
	// Setting the query points
	for (int i = 0; i < tar_y; i++) {
		for (int j = 0; j < tar_x; j++) {
			// Set X[i,j] and Y[i,j]
			X.at<float>(i, j) = float(orig_x) / tar_x * i;
			Y.at<float>(i, j) = float(orig_y) / tar_y * j;
		}
	}
	// Output image
	Mat Output(tar_y, tar_x, CV_8UC1);
	// Performing the interpolation
	for (int i = 0; i < tar_y; i++) {
		for (int j = 0; j < tar_x; j++) {
			// Set Output[i,j] using X[i,j] and Y[i,j]
			int x1 = int(X.at<float>(i, j));
			int x2 = x1 + 1;
			if (x2 > orig_x - 1) { x2 = x1; }
			int y1 = int(Y.at<float>(i, j));
			int y2 = y1 + 1;
			if (y2 > orig_y - 1) { y2 = y1; }
			float xq = X.at<float>(i, j);
			float yq = Y.at<float>(i, j);
			int v1 = int(I.at<uchar>(x1, y1));
			int v2 = int(I.at<uchar>(x2, y1));
			int v3 = int(I.at<uchar>(x1, y2));
			int v4 = int(I.at<uchar>(x2, y2));
			float vq1 = (xq - x1) * v2 + (x2 - xq) * v1;
			float vq2 = (xq - x1) * v4 + (x2 - x1) * v3;
			float vq = (yq - y1) * vq2 + (y2 - yq) * vq1;
			Output.at<uchar>(i, j) = uchar(vq);
		}
	}
	return Output;
}

Mat Dilate(Mat I, Mat elem) {
	Mat Output(I.rows, I.cols, CV_8UC1);
	int h = elem.rows / 2;
	for (int i = 0; i < I.rows; i++) {
		for (int j = 0; j < I.cols; j++) {
			//wr(int(I.at<uchar>(i, j)));
			int im = int(I.at<uchar>(i, j));
			bool dilFlag;
			if (im == 255) {
				dilFlag = true;
			}
			else {
				dilFlag = false;
				for (int ki = -h; ki <= h; ki++) {
					if (i + ki >= 0 && i + ki < I.rows) {
						for (int kj = -h; kj <= h; kj++) {
							if (j + kj >= 0 && j + kj < I.cols) {
								int kr = int(elem.at<uchar>(ki + h, kj + h));
								//wr(im);
								int img = int(I.at<uchar>(i + ki, j + kj));
								if (kr == 255 && img == 255) { dilFlag = true; }
							}
						}
					}
				}
			}
			if (dilFlag == false) { Output.at<uchar>(i, j) = uchar(0); }
			else { Output.at<uchar>(i, j) = uchar(255); }
		}
	}
	return Output;
}

Mat Erode(Mat I, Mat elem) {
	Mat Output(I.rows, I.cols, CV_8UC1);
	int h = elem.rows / 2;
	for (int i = 0; i < I.rows; i++) {
		for (int j = 0; j < I.cols; j++) {
			//wr(int(I.at<uchar>(i, j)));
			int im = int(I.at<uchar>(i, j));
			bool eroFlag;
			if (im == 0) {
				eroFlag = true;
			}
			else {
				eroFlag = false;
				for (int ki = -h; ki <= h; ki++) {
					if (i + ki >= 0 && i + ki < I.rows) {
						for (int kj = -h; kj <= h; kj++) {
							if (j + kj >= 0 && j + kj < I.cols) {
								int kr = int(elem.at<uchar>(ki + h, kj + h));
								//wr(im);
								int img = int(I.at<uchar>(i + ki, j + kj));
								if (kr == 255 && img == 0) { eroFlag = true; }
							}
						}
					}
				}
			}
			if (eroFlag == false) { Output.at<uchar>(i, j) = uchar(255); }
			else { Output.at<uchar>(i, j) = uchar(0); }
		}
	}
	return Output;
}

Mat Open(Mat I, Mat elem) {
	Mat J = Erode(I, elem);
	Mat K = Dilate(J, elem);
	return K;
}

Mat Close(Mat I, Mat elem) {
	Mat J = Dilate(I, elem);
	Mat K = Erode(J, elem);
	return K;
}

void ConnectedHelper(Mat &I, int i, int j, int labelnum) {
	//Mat Out(I.rows, I.cols, CV_8UC1);
	//for (int ik = 0; ik < I.rows; ik++) {
		//for (int jk = 0; jk < I.cols; jk++) {
			//Out.at<uchar>(ik, jk) = I.at<uchar>(ik, jk);
		//}
	//}
	I.at<uchar>(i, j) = uchar(labelnum);
	if (i + 1 < I.rows) {
		if (I.at<uchar>(i + 1, j) == uchar(255)) { ConnectedHelper(I, i + 1, j, labelnum); }
	}
	if (i - 1 >= 0) {
		if (I.at<uchar>(i - 1, j) == uchar(255)) { ConnectedHelper(I, i - 1, j, labelnum); }
	}
	if (j + 1 < I.cols) {
		if (I.at<uchar>(i, j + 1) == uchar(255)) { ConnectedHelper(I, i, j + 1, labelnum); }
	}
	if (j - 1 >= 0) {
		if (I.at<uchar>(i, j - 1) == uchar(255)) { ConnectedHelper(I, i, j - 1, labelnum); }
	}
	//return I;
}

Mat ConnectedComponents(Mat I, Mat elem) {
	Mat Out(I.rows, I.cols, CV_8UC1);
	for (int i = 0; i < I.rows; i++) {
		for (int j = 0; j < I.cols; j++) {
			Out.at<uchar>(i, j) = I.at<uchar>(i, j);
		}
	}
	int labelnum = 1;
	for (int i = 0; i < I.rows; i++) {
		for (int j = 0; j < I.cols; j++) {
			if (Out.at<uchar>(i, j) == uchar(255)) {
				ConnectedHelper(Out, i, j, labelnum);
				labelnum++;
			}
		}
	}
	return Out;
}