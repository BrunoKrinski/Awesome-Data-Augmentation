import cv2
import imageio
import argparse
import imgaug as ia
from imgaug import augmenters as iaa
from albumentations import Blur, CLAHE, ChannelDropout, ChannelShuffle, \
                           CoarseDropout, Downscale, Equalize, FancyPCA, \
                           FromFloat, GaussNoise, GaussianBlur, GlassBlur, \
                           HueSaturationValue, IAAAdditiveGaussianNoise, \
                           IAAEmboss, IAASharpen, IAASuperpixels, ISONoise, \
                           ImageCompression, InvertImg, MedianBlur, MotionBlur,\
                           MultiplicativeNoise, Normalize, Posterize, RGBShift,\
                           RandomBrightnessContrast, RandomFog, RandomGamma,\
                           RandomRain, RandomShadow, RandomSnow, \
                           RandomSunFlare, Solarize, ToFloat, ToGray, ToSepia
from albumentations import CenterCrop, Crop, CropNonEmptyMaskIfExists, \
                           ElasticTransform, Flip, GridDistortion, GridDropout,\
                           HorizontalFlip, IAAAffine, IAACropAndPad, \
                           IAAPiecewiseAffine, LongestMaxSize, \
                           OpticalDistortion, RandomCrop, RandomGridShuffle, \
                           RandomResizedCrop, RandomRotate90, RandomScale, \
                           RandomSizedCrop, Resize, Rotate, ShiftScaleRotate, \
                           SmallestMaxSize, Transpose, VerticalFlip


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str, dest='image_path', 
                        action='store', required=True, help='Path to an image.')
    parser.add_argument('--augmentation', type=str, dest='augmentation', 
                        action='store', required=True, 
                        help='Augmentation to be applied in the image.')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    image_path = args.image_path
    augmentation = args.augmentation

    image = cv2.imread(image_path)
    height, width, channels = image.shape 
    image_name = image_path.split('/')[-1]

    # Pixel Level transforms:

    ## Blur

    if augmentation == 'blur':
        transform = Blur(always_apply=True)

    elif augmentation == 'gaussian_blur':
        transform = GaussianBlur(always_apply=True)

    elif augmentation == 'glass_blur':
        transform = GlassBlur(always_apply=True)

    elif augmentation == 'median_blur':
        transform = MedianBlur(always_apply=True, blur_limit=(18, 25))

    elif augmentation == 'motion_blur':
        transform = MotionBlur(always_apply=True)

    elif augmentation == 'average_blur':
        transform = iaa.AverageBlur(k=(2, 11))
        transformed_image = transform(image=image)

    ####
    
    elif augmentation == 'clahe':
        transform = CLAHE(always_apply=True, tile_grid_size=(64, 64))
        
    elif augmentation == 'channel_droput':
        transform = ChannelDropout(always_apply=True)
        
    elif augmentation == 'channel_shuffle':
        transform = ChannelShuffle(always_apply=True)
        
    elif augmentation == 'coarse_dropout':
        transform = CoarseDropout(always_apply=True, max_holes=100)
        
    elif augmentation == 'downscale':
        transform = Downscale(always_apply=True)
        
    elif augmentation == 'equalize':
        transform = Equalize(always_apply=True)
        
    elif augmentation == 'fancy_pca':
        transform = FancyPCA(always_apply=True, alpha=1.0)
        
    elif augmentation == 'from_float':
        transform = FromFloat(always_apply=True, max_value=127)
        
    elif augmentation == 'gauss_noise':
        transform = GaussNoise(always_apply=True, var_limit=(200.0, 250.0))
    
    elif augmentation == 'hue_saturation':
        transform = HueSaturationValue(always_apply=True)
    
    elif augmentation == 'additive_gaussian_noise':
        transform = IAAAdditiveGaussianNoise(always_apply=True)

    elif augmentation == 'emboss':
        transform = IAAEmboss(always_apply=True, strength=(0.5, 0.8), alpha=1.0)
    
    elif augmentation == 'sharpen':
        transform = IAASharpen(always_apply=True, alpha=1.0)
    
    elif augmentation == 'super_pixels':
        transform = IAASuperpixels(always_apply=True)

    elif augmentation == 'iso_noise':
        transform = ISONoise(always_apply=True, color_shift=(0.08, 0.1), 
                                                intensity=(0.5, 0.8))

    elif augmentation == 'image_compression':
        transform = ImageCompression(always_apply=True, quality_lower=10)

    elif augmentation == 'invert_img':
        transform = InvertImg(always_apply=True)

    elif augmentation == 'multiplicative_noise':
        transform = MultiplicativeNoise(always_apply=True, 
                                        multiplier=(0.5, 1.5))

    elif augmentation == 'normalize':
        transform = Normalize(always_apply=True)
    
    elif augmentation == 'posterize':
        transform = Posterize(always_apply=True, num_bits=2)
    
    elif augmentation == 'rgb_shift':
        transform = RGBShift(always_apply=True)
    
    elif augmentation == 'brightness_contrast':
        transform = RandomBrightnessContrast(always_apply=True, 
                                             brightness_limit=0.5)

    elif augmentation == 'random_fog':
        transform = RandomFog(always_apply=True)

    elif augmentation == 'random_gamma':
        transform = RandomGamma(always_apply=True, gamma_limit=(120, 200))

    elif augmentation == 'random_rain':
        transform = RandomRain(always_apply=True)
    
    elif augmentation == 'random_shadow':
        transform = RandomShadow(always_apply=True)

    elif augmentation == 'random_snow':
        transform = RandomSnow(always_apply=True)

    elif augmentation == 'random_sun_flare':
        transform = RandomSunFlare(always_apply=True)

    elif augmentation == 'solarize':
        transform = Solarize(always_apply=True)

    elif augmentation == 'to_float':
        transform = ToFloat(always_apply=True)
    
    elif augmentation == 'to_gray':
        transform = ToGray(always_apply=True)
    
    elif augmentation == 'to_sepia':
        transform = ToSepia(always_apply=True)

    elif augmentation == 'center_crop':
        transform = CenterCrop(always_apply=True, width=400, height=400)
    
    elif augmentation == 'crop':
        transform = Crop(always_apply=True, x_max=400, y_max=400)

    elif augmentation == 'crop_non_empty_mask':
        transform = CropNonEmptyMaskIfExists(always_apply=True, width=400, 
                                                                height=400)

    elif augmentation == 'elastic_transform':
        transform = ElasticTransform(always_apply=True, alpha=10)

    elif augmentation == 'flip':
        transform = Flip(always_apply=True)

    elif augmentation == 'grid_distortion':
        transform = GridDistortion(always_apply=True, distort_limit=0.5)

    elif augmentation == 'grid_dropout':
        transform = GridDropout(always_apply=True)

    elif augmentation == 'horizontal_flip':
        transform = HorizontalFlip(always_apply=True)

    elif augmentation == 'iaaaffine':
        transform = IAAAffine(always_apply=True, p=1.0, rotate=180, shear=50)

    elif augmentation == 'crop_and_pad':
        transform = IAACropAndPad(always_apply=True, percent=0.5)
    
    elif augmentation == 'longest_max_size':
        transform = LongestMaxSize(always_apply=True)

    elif augmentation == 'optical_distortion':
        transform = OpticalDistortion(always_apply=True, distort_limit=0.5)
    
    elif augmentation == 'random_crop':
        transform = RandomCrop(always_apply=True, width=200, height=200)

    elif augmentation == 'random_grid_shuffle':
        transform = RandomGridShuffle(always_apply=True, grid=(5, 5))

    elif augmentation == 'random_resized_crop':
        transform = RandomResizedCrop(always_apply=True, width=100, height=100)

    elif augmentation == 'random_rotate90':
        transform = RandomRotate90(always_apply=True)

    elif augmentation == 'random_scale':
        transform = RandomScale(always_apply=True)

    elif augmentation == 'random_sized_crop':
        transform = RandomSizedCrop(always_apply=True, height=500, width=500, min_max_height=[200, 200])

    elif augmentation == 'resize':
        transform = Resize(always_apply=True, height=500, width=500)

    elif augmentation == 'rotate':
        transform = Rotate(always_apply=True)

    elif augmentation == 'shift_scale_rotate':
        transform = ShiftScaleRotate(always_apply=True, shift_limit=0.1, 
                                                        scale_limit=0.5)
    
    elif augmentation == 'smallest_max_size':
        transform = SmallestMaxSize(always_apply=True)

    elif augmentation == 'transpose':
        transform = Transpose(always_apply=True)

    elif augmentation == 'vertical_flip':
        transform = VerticalFlip(always_apply=True)

    #transformed_image = transform(image=image)['image']

    name, ext = image_name.split('.')
    new_path = name + '_' + augmentation + '.' + ext
    cv2.imwrite(new_path, transformed_image)