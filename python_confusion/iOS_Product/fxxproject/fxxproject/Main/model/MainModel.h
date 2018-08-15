//
//  MainModel.h
//  fxxproject
//
//  Created by  翁献山 on 2018/8/8.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface MainModel : NSObject
@property (strong,nonatomic) NSString *CrashDelay;
@property (strong,nonatomic) NSString *appName;
@property (strong,nonatomic) NSString *bundleIdentifier;
@property (strong,nonatomic) NSString *isCrash;
@property (strong,nonatomic) NSString *isOverdue;
@property (strong,nonatomic) NSString *lastTime;
@property (strong,nonatomic) NSString *registrationTime;
@property (strong,nonatomic) NSString *state;
@property (strong,nonatomic) NSString *url;
@property (strong,nonatomic) NSString *userIP;

//CrashDelay = 0;
//appName = xxgame;
//bundleIdentifier = "com.fxx.fxxproject";
//isCrash = 0;
//isOverdue = 0;
//lastTime = "2018-08-08 20:47:32";
//registrationTime = "2018-08-08 20:47:32";
//state = 0;
//url = "";
//userIP = "223.73.64.154";
@end
