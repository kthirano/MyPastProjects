MMat FindPDF(Mat I) {

	Mat pdf(256, 1, CV_32FC1);
	for (int i = 0; i < 256; i++) {
		pdf.at<float>(i, 0) = 0.0;
	}


	for (int i = 0; i < I.rows; i++) {
		for (int j = 0; j < I.cols; j++) {
			int num = int(I.at<uchar>(i, j));
			pdf.at<float>(num, 0) += 1;
			// Fill in pdf array
		}
	}

	for (int i = 0; i < 256; i++) {
		pdf.at<float>(i, 0) = pdf.at<float>(i, 0) / (I.rows * I.cols);
	}
	// convert histogram to pdf

	return pdf;

}

Mat FindCDF(Mat pdf) {

	Mat cdf(256, 1, CV_32FC1);

	for (int i = 0; i < 256; i++) {
		cdf.at<float>(i, 0) = pdf.at<float>(i, 0);
		if (i != 0) {
			cdf.at<float>(i, 0) += cdf.at<float>(i - 1, 0);
		}
		// Fill in cdf array
	}

	return cdf;
}

Mat FindEqualMapping(Mat cdf) {

	Mat target(256, 1, CV_32FC1);

	for (int i = 0; i < 256; i++) {
		target.at<float>(i, 0) = i / 256.0;
		// Fill in target cdf
	}

	Mat mapping(256, 1, CV_8UC1);

	for (int i = 0; i < 256; i++) {
		float maxdiff = 256.0;
		int plot;
		// Find closet target[j] to cdf[i]
		for (int j = 0; j < 256; j++) {
			float diff = target.at<float>(j, 0) - cdf.at<float>(i, 0);
			if (diff < 0) {
				diff *= -1;
			}
			if (diff < maxdiff) {
				maxdiff = diff;
				plot = j;
			}
		}

		mapping.at<uchar>(i, 0) = uchar(plot);
	}

	return mapping;
}

Mat ApplyEqualization(Mat I, Mat mapping) {

	Mat Output(I.rows, I.cols, CV_8UC1);

	for (int i = 0; i < I.rows; i++) {

		for (int j = 0; j < I.cols; j++) {
			Output.at<uchar>(i, j) = mapping.at<uchar>(int(I.at<uchar>(i, j)), 0);
			// Set the output[i,j]
		}
	}

	return Output;

}

Mat HistogramEqualization(Mat I) {
	Mat currPDF = FindPDF(I);
	Mat currCDF = FindCDF(currPDF);
	Mat eqMap = FindEqualMapping(currCDF);
	Mat output = ApplyEqualization(I, eqMap);
	return output;
}


Mat Resize(Mat I, float s){

	int orig_x = I.cols;
	int orig_y = I.rows;

	int tar_x = orig_x * s;
	int tar_y = orig_y * s;

	// Query points
	Mat X(tar_y, tar_x, CV_32FC1);
	Mat Y(tar_y, tar_x, CV_32FC1);

	// Setting the query points
	for (int i = 0; i < target_y; i++){

		for (int j = 0; j < target_x; j++){

			// Set X[i,j] and Y[i,j]
		}
	}


	// Output image
	Mat Output(tar_y, tar_x, CV_8UC1);

	// Performing the interpolation
	for (int i = 0; i < target_y; i++){

		for (int j = 0; j < target_x; j++){

			// Set Output[i,j] using X[i,j] and Y[i,j]
		}
	}

	return Output;
}