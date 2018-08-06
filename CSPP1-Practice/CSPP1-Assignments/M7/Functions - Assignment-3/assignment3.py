
Conversation opened. 1 read message.

Skip to content
Using Msitprogram.net Mail with screen readers
in:sent 

Move to Inbox More 
1 of 45
 
assignment code

Pranav Surampudi 20186017 <sharmapranav307@msitprogram.net>
Attachments7:12 PM (2 hours ago)
to rishikaharitha 


-- 
Regards,
Pranav Surampudi
2 Attachments
    
Click here to Reply or Forward
Using 0.5 GB
Program Policies
Powered by Google
Last account activity: 1 hour ago
Details


'''
************************
Author: Pranav Surampudi
Date: 6 August 2018
Encoding: utf-8
************************
'''
def paying_debt_off_in_a_year(balance, annual):
    """Calculate minimum payment by bisection"""
    lower = balance / 12.0
    upper = balance * (1 + annual / 12.0) ** 12 / 12
    fixed = (lower + upper) / 2.0
    i = 1
    while True:
        remain = balance
        for i in range(1, 13):
            remain = (remain - fixed) * (1 + annual / 12.0)
        if remain > 0:
            lower = fixed
        elif remain <= 0 and remain >= -0.03:
            break
        else:
            upper = fixed
        fixed = (lower + upper) / 2.0
    ans = "Lowest Payment: " + str(round(fixed, 2))
    print(ans)
def main():
    """Main Function """
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    paying_debt_off_in_a_year(data[0], data[1])
if __name__ == "__main__":
    main()
assignment3.py
Displaying assignment3.py.