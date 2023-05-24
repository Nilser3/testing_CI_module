from main import extract_nifti_data, threshold_data, get_mean
import nibabel as nib 
import numpy as np
import os 
def test_extract_nifti_data(tmpdir):
    data = np.ones ((32,32,15,100))
    img = nib.Nifti1Image(data, np.eye(4))
    path = os.path.join(tmpdir, "test.nii.gz")
    "my_dir"
    "my_dir/test.nii.gz"
    nib.save(img,path)
    loaded_data = extract_nifti_data(path)
    assert np.array_equal(data, loaded_data), "loading is correct"

def test_threshold():
    data = np.random.randn(4,4)
    threshold = 0.1
    thresholded_data = threshold_data(data,threshold)
    assert (thresholded_data > threshold).all(), "thresholding incorrect "

def test_get_mean():
    data = np.ones((4,4))
    average = get_mean(data)
    assert average ==1 , "mean correct"