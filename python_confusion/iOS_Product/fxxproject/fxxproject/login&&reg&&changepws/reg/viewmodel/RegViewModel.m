//
//  RegViewModel.m
//  fxxproject
//
//  Created by  翁献山 on 2018/8/6.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import "RegViewModel.h"

@implementation RegViewModel
/**
 注册按钮样式
 
 @param Vc 当前视图控制器
 @return 当前viewmodel对象
 */
-(RegViewModel *)setRegbtnStyle:(RegViewController *)Vc{
    Vc.Regbtn.layer.cornerRadius=5;
    Vc.Regbtn.layer.cornerRadius=5;
    Vc.Regbtn.layer.masksToBounds=YES;
    return self;
}
/**
 提交注册资料

 @param Vc 当前视图控制器
 */
-(void)postRegdata:(RegViewController *)Vc{
    if (Vc.UserpswField.text.length==0) {
        [MBProgressHUD showError:@"账号不能为空" toView:Vc.view];
    }else if (Vc.UsernameField.text.length<6){
        [MBProgressHUD showError:@"用户名不能小于6位" toView:Vc.view];
    }
    else if (Vc.UserpswField.text.length==0){
        [MBProgressHUD showError:@"密码不能为空" toView:Vc.view];
    }else if (Vc.UserpswField.text.length<6){
        [MBProgressHUD showError:@"密码不能小于6位" toView:Vc.view];
    }
    else{
        [[FxxNetwork sharedInstance]signup:Vc.UsernameField.text
                                  passWord:Vc.UserpswField.text
                                      view:Vc.view
                                   success:^(id data)
        {
            [MBProgressHUD showSuccess:@"恭喜你注册成功" toView:Vc.view];
            [NSThread sleepForTimeInterval:1];
            [Vc.navigationController popViewControllerAnimated:YES];
            if (Vc.Regblock) {
                Vc.Regblock(Vc.UsernameField.text,Vc.UserpswField.text);
            }
        } failure:^(NSError *error) {
            
        }];
    }
}

@end
