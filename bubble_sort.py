#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
冒泡排序算法实现
Bubble Sort Algorithm Implementation

冒泡排序是一种简单的排序算法，它重复地遍历要排序的列表，
比较相邻的元素并交换它们的位置，直到没有更多的交换需要为止。

时间复杂度：
- 最好情况：O(n) - 当数组已经有序时
- 平均情况：O(n²)
- 最坏情况：O(n²)

空间复杂度：O(1) - 原地排序
"""


def bubble_sort(arr):
    """
    冒泡排序算法
    
    Args:
        arr (list): 需要排序的列表
        
    Returns:
        list: 排序后的列表
    """
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记本轮是否有交换，用于优化
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        # 每轮后最大的元素会"冒泡"到末尾，所以范围逐渐缩小
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果本轮没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    
    return arr


def bubble_sort_with_steps(arr):
    """
    带步骤显示的冒泡排序算法（用于演示）
    
    Args:
        arr (list): 需要排序的列表
        
    Returns:
        list: 排序后的列表
    """
    n = len(arr)
    print(f"原始数组: {arr}")
    
    for i in range(n):
        swapped = False
        print(f"\n第 {i + 1} 轮排序:")
        
        for j in range(0, n - i - 1):
            print(f"  比较 {arr[j]} 和 {arr[j + 1]}", end="")
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f" -> 交换: {arr}")
            else:
                print(f" -> 不交换: {arr}")
        
        if not swapped:
            print("  数组已有序，提前结束")
            break
    
    print(f"\n最终结果: {arr}")
    return arr


def test_bubble_sort():
    """测试冒泡排序算法"""
    print("=" * 50)
    print("冒泡排序算法测试")
    print("=" * 50)
    
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1],  # 逆序
        [1],              # 单个元素
        [],               # 空数组
        [3, 3, 3, 3],     # 相同元素
    ]
    
    for i, test_arr in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}: {test_arr}")
        result = bubble_sort(test_arr.copy())
        print(f"排序结果: {result}")
        print(f"是否正确: {result == sorted(test_arr)}")


if __name__ == "__main__":
    # 运行测试
    test_bubble_sort()
    
    print("\n" + "=" * 50)
    print("冒泡排序步骤演示")
    print("=" * 50)
    
    # 演示排序步骤
    demo_arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_with_steps(demo_arr.copy())