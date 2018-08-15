//
//  ViewController.m
//  fxxproject
//
//  Created by  翁献山 on 2018/8/6.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import "ViewController.h"
#import "LoginView.h"
#import "MainViewModel.h"
#import <WebKit/WebKit.h>
@interface ViewController ()<WKUIDelegate,WKNavigationDelegate>
@property (weak, nonatomic) IBOutlet UIImageView *showImageView;
@property (strong,nonatomic)MainViewModel *ViewModel;
@property (strong,nonatomic) WKWebView *webview;
@property(copy,nonatomic)NSString *URL;
@end

@implementation ViewController
- (void)viewWillAppear:(BOOL)animated
{
    [self.navigationController setNavigationBarHidden:YES animated:YES];
    [super viewWillAppear:animated];
}
-(void)viewWillDisappear:(BOOL)animated{
    [self.navigationController setNavigationBarHidden:NO animated:YES];
    [super viewWillDisappear:animated];
}
- (void)viewDidLoad {
    [super viewDidLoad];
    [[UIApplication sharedApplication] setStatusBarHidden:YES];
    [self.ViewModel Regisdevicebygame:self];
    [self.view addSubview:self.webview];
    self.webview.scrollView.bounces = NO;
    self.webview.UIDelegate = self;
    self.webview.navigationDelegate = self;
    [self.view addSubview:self.showImageView];
    // Do any additional setup after loading the view, typically from a nib.
}
-(WKWebView *)webview{
    if (_webview==nil) {
        _webview = [[WKWebView alloc]initWithFrame:CGRectMake(0, 0, ScreenWidth, ScreenHeight)];
    }
    return _webview;
}
-(MainViewModel *)ViewModel{
    if (_ViewModel==nil) {
        _ViewModel=[[MainViewModel alloc]init];
    }
    return _ViewModel;
}
-(void)request:(NSString *)url{
    [self.webview loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:url]]];
    self.URL = url;
}
//处理跳转
-(void)webView:(WKWebView *)webView decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction decisionHandler:(void (^)(WKNavigationActionPolicy))decisionHandler
{
    if (navigationAction.targetFrame == nil) {
        [webView loadRequest:navigationAction.request];
    }
    NSString* url = [NSString stringWithFormat:@"%@", navigationAction.request.URL];
    NSArray *array = @[@"weixin://",@"alipay://",@"mqqapi://"];
    BOOL isNext = YES;
    for (NSString *xy in array) {
        if([url rangeOfString:xy].length>0){
            isNext = NO;
            [[UIApplication sharedApplication]openURL:[NSURL URLWithString:url]];
            [self request:self.URL];
        }
    }
    decisionHandler(WKNavigationActionPolicyAllow);
}
-(void)webView:(WKWebView *)webView didFinishNavigation:(WKNavigation *)navigation{
    self.showImageView.hidden = YES;
}
- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
