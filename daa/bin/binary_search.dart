void main() {
  final List<int> arr = [1, 56, 76, 45, 64, 67, 5];
  arr.sort();
  int key = 67;
  int minVal = 0;
  int maxVal = arr.length - 1;
  binarySearch(arr, key, minVal, maxVal);
}

void binarySearch(List<int> arr, int key, int minVal, int maxVal) {
  if (maxVal >= minVal) {
    print('minVal $minVal');
    print('maxVal $maxVal');
    int mid = ((maxVal + minVal) / 2).floor();
    // 
    if (key == arr[mid]) {
      print('your item is at index: $mid');
    } else if (key > arr[mid]) {
      binarySearch(arr, key, mid + 1, maxVal);
    } else {
      binarySearch(arr, key, minVal, mid - 1);
    }
  }
}
