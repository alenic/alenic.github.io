---
layout: post
title:  "MNIST Dataset Loader in python"
subtitle: ""
date:   2021-02-8 00:00:00 -0600
categories: snippets
imgpath: ""
keywords: "python, mnist, machine-learning"
code_folder: /assets/code/mnist
---


{% highlight python %}
import urllib.request
import os
import gzip
import struct
import numpy as np

class MNIST(object):
    def __init__(self, dataset_out_dir=".", base_url="http://yann.lecun.com/exdb/mnist/"):
        self.dataset_out_dir = dataset_out_dir
        train_images_file = "train-images-idx3-ubyte.gz"
        train_labels_file = "train-labels-idx1-ubyte.gz"
        test_images_file = "t10k-images-idx3-ubyte.gz"
        test_labels_file = "t10k-labels-idx1-ubyte.gz"

        train_images_path = os.path.join(dataset_out_dir, train_images_file)
        train_labels_path = os.path.join(dataset_out_dir, train_labels_file)
        test_images_path = os.path.join(dataset_out_dir, test_images_file)
        test_labels_path = os.path.join(dataset_out_dir, test_labels_file)

        self.download(base_url + train_images_file, train_images_path)
        self.download(base_url + test_images_file, train_labels_path)
        self.download(base_url + train_labels_file, test_images_path)
        self.download(base_url + test_labels_file, test_labels_path)
        
        self.train_images = self.parse_images(train_images_path)
        self.train_labels = self.parse_labels(train_labels_path)
        self.test_images = self.parse_images(test_images_path)
        self.test_labels = self.parse_labels(test_labels_path)
    
    def download(self, url, output):
        print("Downloading", url, "to", output, "...")
        os.makedirs(self.dataset_out_dir, exist_ok=True)
        if not os.path.exists(output):
            urllib.request.urlretrieve(url, output)

    def parse_images(self, f):
        images = []
        with gzip.open(f, 'rb') as fp:
            header = struct.unpack('>4i', fp.read(16))
            magic, size, width, height = header

            if magic != 2051:
                raise RuntimeError("'%s' is not an MNIST image set." % f)
            
            chunk = width * height
            for _ in range(size):
                img = struct.unpack('>%dB' % chunk, fp.read(chunk))
                img_np = np.array(img, np.uint8)
                images.append(img_np)

        return images


    def parse_labels(self, f):
        with gzip.open(f, 'rb') as fp:
            header = struct.unpack('>2i', fp.read(8))
            magic, size = header

            if magic != 2049:
                raise RuntimeError("'%s' is not an MNIST label set." % f)
            
            labels = struct.unpack('>%dB' % size, fp.read())
        
        return np.array(labels, np.int32)


if __name__ == "__main__":
    mnist = MNIST(dataset_out_dir="mnist")

    print("train dataset")
    for label, perc in enumerate(np.histogram(mnist.train_labels, normed=True)[0]):
        print("%d: %.2f %%" % (label, 100*perc))

    print("test dataset")
    for label, perc in enumerate(np.histogram(mnist.test_labels, normed=True)[0]):
        print("%d: %.2f %%" % (label, 100*perc))


{% endhighlight %}
