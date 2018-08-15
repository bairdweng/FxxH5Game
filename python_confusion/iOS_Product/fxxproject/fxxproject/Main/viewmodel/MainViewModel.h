//
//  MainViewModel.h
//  fxxproject
//
//  Created by  翁献山 on 2018/8/8.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "ViewController.h"
#import "LoginView.h"
#import "MainModel.h"
@interface MainViewModel : NSObject
@property (strong,nonatomic) MainModel *Model;
@property (strong,nonatomic) LoginView *loginview;
-(void)Regisdevicebygame:(ViewController *)Vc;
-(void)Getloginview:(ViewController *)Vc;
@end
