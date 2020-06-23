Mat CreateGaussianFilter() {
	Mat I(5, 5, CV_32FC1);
	// This is 1D Gaussian kernel values
	float g[] = { 0.05, 0.25, 0.4, 0.25, 0.05 };
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			// Fill in the kernel values
			I.at<float>(i, j) = g[i] * g[j];
		}
	}
	return I;
}

Mat ApplyFilter(Mat input, Mat filter) {
	// This is your empty output Mat
	Mat output(input.rows, input.cols, CV_8UC1);
	for (int i = 0; i < output.rows; i++) {
		for (int j = 0; j < output.cols; j++) {
			// Perform convolution for this pixel
			float total = 0.0;
			for (int filterIterR = 0; filterIterR < filter.rows; filterIterR++) {
				for (int filterIterC = 0; filterIterC < filter.cols; filterIterC++) {
					int rowFactor = filterIterR - filter.rows / 2;
					int colFactor = filterIterC - filter.cols / 2;
					int rowAccess = i + rowFactor;
					if (rowAccess < 0) { rowAccess = 0; }
					if (rowAccess >= output.rows) { rowAccess = output.rows - 1; }
					int colAccess = j + colFactor;
					if (colAccess < 0) { colAccess = 0; }
					if (colAccess >= output.cols) { colAccess = output.cols - 1; }
					total += float(input.at<uchar>(rowAccess, colAccess)) * filter.at<float>(filterIterR.filterIterC);
				}
			}
			// Assign the output value for pixel
			output.at<uchar>(i, j) = uchar(total);
		}
	}

	return output;
}

Mat Reduce(Mat input) {

	// This is your empty output image
	Mat output(input.rows / 2, input.cols / 2, CV_8UC1);
	// Calculate each pixel of output image
	for (int i = 0; i < output.rows; i++) {
		for (int j = 0; j < output.cols; j++) {
			output.at<uchar>(i, j) = uchar((float(input.at<uchar>(i * 2, j * 2)) + float(input.at<uchar>(i * 2 + 1, j * 2)) + float(input.at<uchar>(i * 2, j * 2 + 1)) + float(input.at<uchar>(i * 2 + 1, j * 2 + 1))) / 4.0);
		}
	}
	return output;
}

Mat Deduct(Mat I, Mat J) {
	// Intermediate pixel to keep the differences
	// Each entry is int
	Mat intermediate(I.rows, I.cols, CV_32SC1);
	int minVal = 256;
	int maxVal = -256;
	for (int i = 0; i < intermediate.rows; i++) {
		for (int j = 0; j < intermediate.cols; j++) {
			/*
				Calculate the intermediate pixel values
			*/
			int diff = int(I.at<uchar>(i, j)) - int(J.at<uchar>(i, j));
			intermediate.at<int>(i, j) = diff;
			if (diff < minVal) {
				minVal = diff;
			}
			if (diff > maxVal) {
				maxVal = diff;
			}
		}
	}
	float dynamicRange = maxVal - minVal;

	// The output image of type unsigned char for each pixel
	Mat result(I.rows, I.cols, CV_8UC1);
	for (int i = 0; i < result.rows; i++) {
		for (int j = 0; j < result.cols; j++) {
			/*
			// Calculate the output pixels
			result.at<uchar>(i, j) = ...
			*/
			result.at<uchar>(i, j) = uchar(255 * float(intermediate.at<int>(i, j) - minVal) / dynamicRange);
		}
	}

	return result;
}