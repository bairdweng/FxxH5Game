//
//  MainViewModel.m
//  fxxproject
//
//  Created by  翁献山 on 2018/8/8.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import "MainViewModel.h"
#import "RegViewController.h"
#import "LoginModel.h"
@implementation MainViewModel
-(void)Regisdevicebygame:(ViewController *)Vc{
    __weak typeof(self) weakself = self;
   NSString *app_Name = [[[NSBundle mainBundle] infoDictionary] objectForKey:@"CFBundleDisplayName"];
   NSString *app_build = [[[NSBundle mainBundle] infoDictionary] objectForKey:@"CFBundleIdentifier"];
   
    [[FxxNetwork sharedInstance]Regisdevicebygame:app_Name
                                 bundleidentifier:app_build
                                          needURL:@"1"
                                             view:Vc.view
                                          success:^(id data)
    {
        
        
        weakself.Model =[MainModel mj_objectWithKeyValues:data];
        if ([weakself.Model.state integerValue]==1) {
            [Vc request:weakself.Model.url?:@"https://www.baidu.com/"];
        }else{
            [weakself Getloginview:Vc];
        }
    } failure:^(NSError *error) {

    }];
}

-(void)Getloginview:(ViewController *)Vc{
    __weak typeof(self) weakself = self;
    NSArray *xib =[[NSBundle mainBundle]loadNibNamed:@"LoginView"
                                               owner:nil
                                             options:nil];
    self.loginview =[xib firstObject];
    self.loginview.frame=Vc.view.bounds;
    self.loginview.UserNameField.text=[[NSUserDefaults standardUserDefaults]objectForKey:@"UserNameField"];
    self.loginview.UserPswField.text=[[NSUserDefaults standardUserDefaults]objectForKey:@"UserPswField"];
    [Vc.view addSubview:_loginview];
    self.loginview.btnsenderblock = ^(NSInteger index) {
        switch (index) {
            case 0:{
                RegViewController *Regvc=[[RegViewController alloc]init];
                [Vc.navigationController pushViewController:Regvc animated:YES];
                Regvc.Regblock = ^(NSString*Username,NSString* Uerpsw) {
                    [weakself login:Vc username:Username psw:Uerpsw];
                };
            }
                break;
            case 1:
                break;
            case 2:{
                if (weakself.loginview.UserNameField.text.length==0) {
                    [MBProgressHUD showError:@"用户名不能为空" toView:Vc.view];
                }else if (weakself.loginview.UserPswField.text.length==0){
                    [MBProgressHUD showError:@"密码不能为空"
                                      toView:Vc.view];
                }else{
                    [weakself login:Vc
                           username:weakself.loginview.UserNameField.text
                                psw:weakself.loginview.UserPswField.text];
                }
            }
                break;
            default:
                break;
        }
    };
    [self.loginview changeloginviewheight:YES];
}
-(void)login:(ViewController *)vc
    username:(NSString *)username
         psw:(NSString *)psw{
    __weak typeof(self) weakself = self;
    [[FxxNetwork sharedInstance]gamelogin:username
                                 passWord:psw
                                     view:vc.view
                                  success:^(id data)
     {
         [MBProgressHUD showSuccess:@"登录成功" toView:vc.view];
         LoginModel*mode=[LoginModel mj_objectWithKeyValues:data];
         [[NSUserDefaults standardUserDefaults]setObject:username forKey:@"UserNameField"];
         [[NSUserDefaults standardUserDefaults]setObject:psw forKey:@"UserPswField"];
         if ([mode.state integerValue]==1) {
             [weakself.loginview changeloginviewheight:NO];
             dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(0.5 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
                 weakself.loginview.alpha=0;
             });
             [vc request:self.Model.url];
         }
    } failure:^(NSError *error) {
        
    }];
}
@end
