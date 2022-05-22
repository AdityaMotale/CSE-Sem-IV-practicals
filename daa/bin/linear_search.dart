void main(List<String> arguments) {
  final List<int> numbers = [1, 56, 76, 45, 64, 67, 5];
  final int key = 67;
  linearSearch(key: key, numbers: numbers);
}

void linearSearch({required int key, required List<int> numbers}) {
  for (int i = 0; i < numbers.length; i++) {
    if (numbers[i] == key) {
      print("Element found at index $i");
    }
  }
}

