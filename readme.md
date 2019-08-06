# ReadMe

## Intro

The Script based on [SusanRTTI](https://github.com/nccgroup/SusanRTTI) , implements a Class that can analyze some programs in batches, and annotates its offset and parameter types to generate a txt file.

The initial development goal was to sort out the callable functions of the **np*.dll** file.

Currently **Windows 32-bit IDA** is used by default. If you need to use **64-bit IDA**, you need to modify the related fields in **run.py** and **msvc.py**.

## Use

Please change the **run32yFilePath**, **pluginPath**, **filePath** fields in **run.py** before using it.

```
python run.py
```

For example, the **dlls** folder contains **test.dll** and **myplugin.dll**. After executing the script, we will get:

```
test.dll
test.idb
test.txt
myplugin.dll
myplugin.idb
myplugin.txt
```

In the **txt** file, such as:

```
0x10021aec	UploadCtrlGetPhotoCount	int __stdcall(int, int, int)
0x10021af8	UploadCtrlSetWaterPressUrl	int __stdcall(int, OLECHAR *strIn, int)
0x10021b04	UploadCtrlSetWaterPressName	int __stdcall(int, OLECHAR *strIn, int)
0x10021b10	UploadCtrlStartUploadSliently	int __stdcall(int, int, int)
0x10021b1c	UploadCtrlStopUploadSliently	int __stdcall(int, int, int)
0x10021b28	UploadCtrlSetRetryTimes	int __stdcall(int, int, int)
0x10021b34	UploadCtrlSetMinSpeed	int __stdcall(int, int, int)
0x10021b40	UploadCtrlUpload	int __stdcall(int, int, int)
```

We get the parameter type of the function, but the actual number of parameters is not accurate and needs to be analyzed according to the offset **IDA**.

We can also get **log** after modifying **run.py**.

## Extra

It can be used as a **ida plugin**.

```
File -> Script File -> classinformer.py
```

Maybe you need remove this from **classinformer**:

```
Line 16: idc.Exit(0)
```

