## Code descriptions:

What we can learn from this code:
- The `psutil` module has a `disk_partitions` function that will return a list of all available partitions(drives) on our system. Each element in the list is a type of `sdiskpart`. For instance, 1 element of each `sdiskpart` can look like this:
 - On Windows system: 
 ```python
sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260)
```
 - On Linux system:
 ```python
sdiskpart(device='/dev/nvme0n1p3', mountpoint='/', fstype='ext4', opts='rw,relatime,errors=remount-ro', maxfile=255, maxpath=4096)
```

- The `psutil` module has a `disk_usage` function too that we can use instead of the `shutil.disk_usage` function! The `psutil.disk_usage` function also calculates the used percentage of disk and I used it where I printed partitions stats! ✌️


- Explaining this part of the code: 
```python
for pa in psutil.disk_partitions(all=False) if pa.opts.find('rw') != -1
```
 - ` all=False`: Will make sure to return physical devices only. ([Documentation](https://psutil.readthedocs.io/en/latest/#psutil.disk_partitions "Documentation"))
 - `pa.opts.find('rw') != -1`: The only way (until now) I found to detect main partitions on Linux, is to check if they have **'rw'** permission or not!? Unfortunately, This will return the '**boot**' partition too. If we want, we can add extra criteria to omit it.
- The `psutil` module has many more useful functions that you can read about [on this page](https://psutil.readthedocs.io/en/latest/).
- I used the `any` function in my code! It returns *True* if any of the elements of a given iterable( List, Dictionary, Tuple, set, etc) are *True* else it returns *False*. You can read more about it with sample codes [on this page](https://www.geeksforgeeks.org/python-any-function/).
- I made a small change in both `check_disk_usage` and `check_cpu_usage` functions to return a `tuple` type!
- I used **List comprehension** that we learned from the previous course at this line of code: 
```python
[(pa.mountpoint, check_disk_usage(pa.device)) for pa in psutil.disk_partitions(all=False) if pa.opts.find('rw') != -1]
```
In the above code, I created a List of Tuples from all available partitions. Each tuple has 2 elements, 1st: a Partition path in `string` type and 2nd: is another `Tuple` based on the return value of the `check_disk_usage` function.
- Instead of using `20` and `75` integer numbers like in the original code, I used constant variables. Using numbers without constant variables is usually called **Magic Numbers**!

## Results:

Output result of running this code on my Windows:

    E:\ has 18.92% only free space.
    U:\ has 15.66% only free space.
    CPU is working properly at 24.2%.
    --------------------
    Partitions stats:
    Partition: 'C:\' Space Used: '71.80'%
    Partition: 'D:\' Space Used: '55.20'%
    Partition: 'E:\' Space Used: '81.10'% Not Healthy
    Partition: 'O:\' Space Used: '77.80'%
    Partition: 'R:\' Space Used: ' 3.20'%
    Partition: 'S:\' Space Used: '67.90'%
    Partition: 'U:\' Space Used: '84.30'% Not Healthy
 

and on My Linux system (I have 2 usable partitions):
    
	All partitions have enough free space.
    CPU is working properly at 10.2%.
    --------------------
    Partitions stats:
    Partition: '/' Space Used: '47.10'%
    Partition: '/boot/efi' Space Used: ' 1.20'%
    Partition: '/media/reza/Data' Space Used: ' 2.70'%
