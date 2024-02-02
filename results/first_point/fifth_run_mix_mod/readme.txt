Ho mixato le modifiche fatte con le augmentation con encoding_position=True

   augment_transform = transforms.Compose([
        transforms.RandomResizedCrop(res, scale=(1, 1)),
        transforms.RandomPerspective(fill=1, p=0.8, distortion_scale=0.5),
        transforms.RandomVerticalFlip(p=0.5), #AGGIUNTA
        transforms.RandomRotation(degrees=15), #AGGIUNTA
        clip_normalizer
    ])