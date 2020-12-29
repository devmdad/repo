{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read Instructions carefully before attempting this assignment\n",
    "\n",
    "# 1) don't rename any function name\n",
    "# 2) don't rename any variable name\n",
    "# 3) don't remove any #comment \n",
    "# 4) don't remove \"\"\" under triple quate values \"\"\"\n",
    "# 5) you have to write code where you found \"write your code here\"\n",
    "# 6) after download rename this file with this format \"PIAICCompletRollNumber_AssignmentNo.py\"\n",
    "#   Example piaic17896_Assignment1.py\n",
    "# 7) After complete this assignment please push on your own GitHub repository.\n",
    "# 8) you can submit this assignment through the google form\n",
    "# 9) copy this file absolute URL then paste in the google form\n",
    "#  The example above: https://github.com/EnggQasim/Batch04_to_35/blob/main/Sunday/1_30%20to%203_30/Assignments/assignment1.txt\n",
    "\n",
    "# * Because all assignment we will be checked through software if you missed any above points \n",
    "# * then we can't assign your scores in our database."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment No : 2\n",
    "Name: Rizwan Saddique\n",
    "Father Name: Muhammad Saddique\n",
    "Batch AIC # 9 2020\n",
    "RollNumber PIAIC99311\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2]\n",
      " [ 3  4]\n",
      " [ 5  6]\n",
      " [ 7  8]\n",
      " [ 9 10]\n",
      " [11 12]]\n"
     ]
    }
   ],
   "source": [
    "# Task no 1\n",
    "def function1():\n",
    "    # create 2d array from 1,12 range \n",
    "    # dimension should be 6row 2 columns  \n",
    "    # and assign this array values in x values in x variable\n",
    "    # Hint: you can use arange and reshape numpy methods  \n",
    "    x =  np.arange(1,13).reshape((6,2)) \n",
    "\n",
    "    return x\n",
    "    \"\"\"\n",
    "    expected output:\n",
    "    [[ 1  2]\n",
    "    [ 3  4]\n",
    "    [ 5  6]\n",
    "    [ 7  8]\n",
    "    [ 9 10]\n",
    "    [11 12]]\n",
    "    \"\"\"\n",
    "print(function1())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[10., 11., 12.],\n",
       "        [13., 14., 15.],\n",
       "        [16., 17., 18.]],\n",
       "\n",
       "       [[19., 20., 21.],\n",
       "        [22., 23., 24.],\n",
       "        [25., 26., 27.]],\n",
       "\n",
       "       [[28., 29., 30.],\n",
       "        [31., 32., 33.],\n",
       "        [34., 35., 36.]]])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Task2\n",
    "def function2():\n",
    "    #create 3D array (3,3,3)\n",
    "    #must data type should have float64\n",
    "    #array value should be satart from 10 and end with 36 (both included)\n",
    "    # Hint: dtype, reshape \n",
    "    \n",
    "    x = np.arange(1,28,dtype=np.float64).reshape((3,3,3))     #wrtie your code here\n",
    "    x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))\n",
    "\n",
    "\n",
    "    return x\n",
    "    \"\"\"\n",
    "    Expected: out put\n",
    "array([[[10., 11., 12.],\n",
    "        [13., 14., 15.],\n",
    "        [16., 17., 18.]],\n",
    "\n",
    "       [[19., 20., 21.],\n",
    "        [22., 23., 24.],\n",
    "        [25., 26., 27.]],\n",
    "\n",
    "       [[28., 29., 30.],\n",
    "        [31., 32., 33.],\n",
    "        [34., 35., 36.]]])    \n",
    "    \"\"\"\n",
    "function2()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 35,  70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,\n",
       "       490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,\n",
       "       945, 980])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#task3\n",
    "def function3():\n",
    "    #extract those numbers from given array. those are must exist in 5,7 Table\n",
    "    #example [35,70,105,..]\n",
    "    a = np.arange(1, 100*10+1).reshape((100,10))\n",
    "    x =  a[(a%5==0) & (a%7==0)] #wrtie your code here\n",
    "    return x\n",
    "    \"\"\"\n",
    "    Expected Output:\n",
    "     [35,  70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,\n",
    "       490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,\n",
    "       945, 980] \n",
    "    \"\"\" \n",
    "function3()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 0, 2],\n",
       "       [4, 3, 5],\n",
       "       [7, 6, 8]])"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#task4\n",
    "def function4():\n",
    "    #Swap columns 1 and 2 in the array arr.\n",
    "   \n",
    "    arr = np.arange(9).reshape(3,3)\n",
    "    arr[::,[0,1]]=arr[::,[1,0]]\n",
    "    \n",
    "  \n",
    "    return arr #wrtie your code here\n",
    "    \"\"\"\n",
    "    Expected Output:\n",
    "          array([[1, 0, 2],\n",
    "                [4, 3, 5],\n",
    "                [7, 6, 8]])\n",
    "    \"\"\" \n",
    "function4()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 0, 0, 0, 0],\n",
       "       [0, 0, 0, 0, 0],\n",
       "       [0, 0, 0, 0, 0],\n",
       "       [0, 0, 0, 0, 0]])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#task5\n",
    "def function5():\n",
    "    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function\n",
    "   \n",
    "    z = np.zeros((4,5))#wrtie your code here\n",
    "    z = z.astype(np.int32)\n",
    "  \n",
    "    return z\n",
    "    \"\"\"\n",
    "    Expected Output:\n",
    "          array([[0, 0, 0, 0, 0],\n",
    "                [0, 0, 0, 0, 0],\n",
    "                [0, 0, 0, 0, 0],\n",
    "                [0, 0, 0, 0, 0]])\n",
    "    \"\"\" \n",
    "function5()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  0,  0,  0, 10],\n",
       "       [ 0,  0, 20,  0,  0]])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#task6\n",
    "def function6():\n",
    "    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively\n",
    "   \n",
    "    arr = np.zeros([2,5])#wrtie your code here\n",
    "    arr = arr.astype(np.int32)\n",
    "    arr[0,4] = 10\n",
    "    arr[1,2] = 20\n",
    "    return arr\n",
    "\n",
    "function6()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def function7():\n",
    "    #  Create an array of zeros with the same shape and type as X. Dont use reshape method\n",
    "    x = np.arange(4, dtype=np.int64)\n",
    "    x[x>0] =0\n",
    "\n",
    "  \n",
    "    return x #write your code here\n",
    "\n",
    "    \"\"\"\n",
    "    Expected Output:\n",
    "          array([0, 0, 0, 0], dtype=int64)\n",
    "    \"\"\" \n",
    "function7()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[6, 6, 6, 6, 6],\n",
       "       [6, 6, 6, 6, 6]])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#task8\n",
    "def function8():\n",
    "    # Create a new array of 2x5 uints, filled with 6.\n",
    "    \n",
    "    x = np.ones((2,5))#write your code here\n",
    "    x = x.astype(np.int32)\n",
    "    x[x>0]=6\n",
    "  \n",
    "    return x\n",
    "    \"\"\"\n",
    "     Expected Output:\n",
    "              array([[6, 6, 6, 6, 6],\n",
    "                     [6, 6, 6, 6, 6]], dtype=uint32)\n",
    "     \"\"\"\n",
    "\n",
    "      \n",
    "function8()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,  24,  26,\n",
       "        28,  30,  32,  34,  36,  38,  40,  42,  44,  46,  48,  50,  52,\n",
       "        54,  56,  58,  60,  62,  64,  66,  68,  70,  72,  74,  76,  78,\n",
       "        80,  82,  84,  86,  88,  90,  92,  94,  96,  98, 100])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#task9\n",
    "def function9():\n",
    "    # Create an array of 2, 4, 6, 8, ..., 100.\n",
    "    \n",
    "    a = np.arange(2,101,2)# write your code here\n",
    "  \n",
    "    return a\n",
    "    \"\"\"\n",
    "     Expected Output:\n",
    "              array([  2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,  24,  26,\n",
    "                    28,  30,  32,  34,  36,  38,  40,  42,  44,  46,  48,  50,  52,\n",
    "                    54,  56,  58,  60,  62,  64,  66,  68,  70,  72,  74,  76,  78,\n",
    "                    80,  82,  84,  86,  88,  90,  92,  94,  96,  98, 100])\n",
    "     \"\"\" \n",
    "\n",
    "     \n",
    "function9()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 2 2]\n",
      " [2 2 2]\n",
      " [2 2 2]]\n"
     ]
    }
   ],
   "source": [
    "#task10\n",
    "def function10():\n",
    "    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.\n",
    "    \n",
    "    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])\n",
    "    brr = np.array([1,2,3])\n",
    "    subt = arr.T-brr# write your code here \n",
    "  \n",
    "    return subt\n",
    "    \"\"\"\n",
    "     Expected Output:\n",
    "               array([[2 2 2]\n",
    "                      [2 2 2]\n",
    "                      [2 2 2]])\n",
    "     \"\"\" \n",
    "\n",
    "     \n",
    "print(function10())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#task11\n",
    "def function11():\n",
    "    # Replace all odd numbers in arr with -1 without changing arr.\n",
    "    \n",
    "    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])\n",
    "    ans = np.where(arr%2!=0,-1,arr) #write your code here \n",
    "  \n",
    "    return ans\n",
    "    \"\"\"\n",
    "     Expected Output:\n",
    "              array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])\n",
    "     \"\"\"\n",
    "     \n",
    "function11()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 1 1 2 2 2 3 3 3 1 2 3 1 2 3 1 2 3]\n"
     ]
    }
   ],
   "source": [
    "#task12\n",
    "def function12():\n",
    "    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.\n",
    "    # HINT: use stacking concept\n",
    "    \n",
    "    arr = np.array([1,2,3])\n",
    "    ans = np.r_[np.repeat(arr,3),np.tile(arr,3)]#write your code here \n",
    "     \n",
    "  \n",
    "    return ans\n",
    "\"\"\"\n",
    "     Expected Output:\n",
    "              array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])\n",
    "     \"\"\"\n",
    "      \n",
    "print(function12())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([6, 9])"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#task13\n",
    "def function13():\n",
    "    # Set a condition which gets all items between 5 and 10 from arr.\n",
    "    \n",
    "    \n",
    "    arr = np.array([2, 6, 1, 9, 10, 3, 27])\n",
    "    ans = arr[(arr>5)&(arr<10)]#write your code here \n",
    "  \n",
    "    return ans\n",
    "    \"\"\"\n",
    "     Expected Output:\n",
    "              array([6, 9])\n",
    "     \"\"\"\n",
    "\n",
    "      \n",
    "function13()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[array([[10, 11, 12]]), array([[13, 14, 15],\n",
      "       [16, 17, 18]]), array([[19, 20, 21],\n",
      "       [22, 23, 24]]), array([[25, 26, 27],\n",
      "       [28, 29, 30]]), array([[31, 32, 33]])]\n"
     ]
    }
   ],
   "source": [
    "#task14\n",
    "def function14():\n",
    "    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.\n",
    "    # Hint use split method\n",
    "    \n",
    "    \n",
    "    arr = np.arange(10, 34, 1) #write reshape code\n",
    "    #ans = np.reshape((8,3))\n",
    "    \n",
    "    #ans = #write your code here \n",
    "    ans = arr.reshape(8,3)\n",
    "    ans = np.split(ans,[1,3,5,7])\n",
    "    return ans\n",
    "\"\"\"\"\n",
    "    Expected Output:\n",
    "    [array([[10, 11, 12],[13, 14, 15]]), \n",
    "    array([[16, 17, 18],[19, 20, 21]]), \n",
    "    array([[22, 23, 24],[25, 26, 27]]), \n",
    "    array([[28, 29, 30],[31, 32, 33]])]\n",
    "    \"\"\" \n",
    "     \n",
    "\n",
    "    \n",
    "print(function14())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-4,  1,  7],\n",
       "       [ 8,  2, -2],\n",
       "       [ 6,  3,  9]])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#task15\n",
    "def function15():\n",
    "    #Sort following NumPy array by the second column\n",
    "    \n",
    "    \n",
    "    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])\n",
    "    ans =  arr[np.argsort(arr[::,1])]#write your code here \n",
    "  \n",
    "    return ans\n",
    "\n",
    "\"\"\"\n",
    "     Expected Output:\n",
    "           array([[-4,  1,  7],\n",
    "                   [ 8,  2, -2],\n",
    "                   [ 6,  3,  9]])\n",
    "     \"\"\" \n",
    "function15()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[1 2]]\n",
      "\n",
      " [[2 3]]\n",
      "\n",
      " [[3 4]]]\n"
     ]
    }
   ],
   "source": [
    "#task16\n",
    "def function16():\n",
    "    #Write a NumPy program to join a sequence of arrays along depth.\n",
    "    \n",
    "    \n",
    "    x = np.array([[1], [2], [3]])\n",
    "    y = np.array([[2], [3], [4]])\n",
    "    ans =  np.dstack((x,y))#write your code here \n",
    "  \n",
    "    return ans\n",
    "\"\"\"\n",
    "Expected Output:\n",
    "                [[[1 2]]\n",
    "\n",
    "                 [[2 3]]\n",
    "\n",
    "                 [[3 4]]]\n",
    "     \n",
    "     \"\"\"\n",
    "\n",
    "\n",
    "\n",
    "  \n",
    "print(function16())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
       "       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
       "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],\n",
       "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
       "       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
       "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],\n",
       "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
       "       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
       "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],\n",
       "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']],\n",
       "      dtype='<U3')"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def function17():\n",
    "    # replace numbers with \"YES\" if it divided by 3 and 5\n",
    "    # otherwise it will be replaced with \"NO\"\n",
    "    # Hint: np.where\n",
    "    arr = np.arange(1,10*10+1).reshape((10,10))\n",
    "    arr1=np.where((arr%3==0)&(arr%5==0),'YES','NO')\n",
    "    return  arr1        # Write Your Code HERE\n",
    "#Excpected Out\n",
    "\"\"\"\n",
    "array([['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
    "       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
    "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],\n",
    "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
    "       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
    "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],\n",
    "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
    "       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],\n",
    "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],\n",
    "       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']],\n",
    "      dtype='<U3')\n",
    "\"\"\"\n",
    "function17()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Task18\n",
    "def function18():\n",
    "    # count values of \"students\" are exist in \"piaic\"\n",
    "    piaic = np.arange(100)\n",
    "    students = np.array([5,20,50,200,301,7001])\n",
    "    x = 0 # Write you code Here\n",
    "    arr=[]\n",
    "    for i in range(len(students)):\n",
    "        arr.append(np.where(piaic==students[i])[0])\n",
    "        if len(arr[i])>0:\n",
    "            x=x+1\n",
    "    return x\n",
    " #Expected output: 3\n",
    "function18()\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  6  17  38  69 110]\n",
      " [ 17  54 101 158 225]\n",
      " [ 38 101 174 257 350]\n",
      " [ 69 158 257 366 485]\n",
      " [110 225 350 485 630]]\n"
     ]
    }
   ],
   "source": [
    "# Task19\n",
    "def function19():\n",
    "    #Create variable \"X\" from 1,25 (both are included) range values\n",
    "    #Convert \"X\" variable dimension into 5 rows and 5 columns\n",
    "    #Create one more variable \"W\" copy of \"X\"\n",
    "    #Swap \"W\" row and column axis (like transpose)\n",
    "    # then create variable \"b\" with value equal to 5\n",
    "    # Now return output as \"(X*W)+b:\n",
    "\n",
    "    X =np.arange(1,26).reshape(5,5)   # Write your code here\n",
    "    W =np.copy(X).T   # Write your code here\n",
    "    b =5   # Write your code here\n",
    "    output =(X*W)+b    # Write your code here\n",
    "    return output\n",
    "#expected output\n",
    "\"\"\"\"\n",
    "array([[  6,  17,  38,  69, 110],\n",
    "       [ 17,  54, 101, 158, 225],\n",
    "       [ 38, 101, 174, 257, 350],\n",
    "       [ 69, 158, 257, 366, 485],\n",
    "       [110, 225, 350, 485, 630]])\n",
    "       \"\"\"\n",
    "print(function19())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Task20\n",
    "def function20():\n",
    "    #apply fuction \"abc\" on each value of Array \"X\"\n",
    "    x = np.arange(1,11)\n",
    "    def abc(x):\n",
    "        return x*2+3-2\n",
    "\n",
    "    return abc(x) #Write your Code here\n",
    "function20()\n",
    "#Expected Output: array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])\n",
    "#--------------------------X-----------------------------X-----------------------------X----------------------------X---------------------\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}