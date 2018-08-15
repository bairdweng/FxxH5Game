//
//  RegViewController.h
//  fxxproject
//
//  Created by  翁献山 on 2018/8/6.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface RegViewController : UIViewController
@property (weak, nonatomic) IBOutlet UITextField *UsernameField;
@property (weak, nonatomic) IBOutlet UITextField *UserpswField;
@property (weak, nonatomic) IBOutlet UIButton *Regbtn;
@property (copy,nonatomic) void(^Regblock)(NSString*Username,NSString* Uerpsw);

@end
