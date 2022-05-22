void main(List<String> args) {
  final List<int> unorderedList = [7, 2, 1, 8, 6, 3, 5, 4];
  final int n = unorderedList.length - 1;
  final List<int> orderedList = quickSort(
    list: unorderedList,
    high: n,
  );
  print(orderedList);
}

/// Swapping
void swap(List list, int i, int j) {
  int temp = list[i];
  list[i] = list[j];
  list[j] = temp;
}

int divideList(List<int> list, int high, int low) {
  if (list.isEmpty) {
    return 0;
  }

  int p = list[high];
  int j = low - 1;

  for (int i = low; i < high; i++) {
    if (list[i] < p) {
      j++;
      swap(list, j, i);
    }
  }
  swap(list, j + 1, high);
  return j + 1;
}

// List<int>
List<int> quickSort({
  required List<int> list,
  required int high,
  int low = 0,
}) {
  if (low < high) {
    int divide = divideList(list, high, low);

    quickSort(list: list, high: divide - 1, low: low);
    quickSort(list: list, high: divide - 1, low: divide + 1);
  }
  return list;
}
