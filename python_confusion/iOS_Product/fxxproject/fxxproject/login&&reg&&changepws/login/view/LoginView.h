//
//  LoginView.h
//  fxxproject
//
//  Created by  翁献山 on 2018/8/6.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface LoginView : UIView
@property (weak, nonatomic) IBOutlet NSLayoutConstraint *loginviewLayoutConstraint;
@property (weak, nonatomic) IBOutlet UIView *loginview;
@property (weak, nonatomic) IBOutlet UIButton *loginbtn;
@property (weak, nonatomic) IBOutlet UITextField *UserNameField;
@property (weak, nonatomic) IBOutlet UITextField *UserPswField;

/**
 tag (0注册 1 忘记密码 2登录)
 */
@property (copy,nonatomic) void(^btnsenderblock)(NSInteger index);
-(void)changeloginviewheight:(BOOL )isshow;

@end
