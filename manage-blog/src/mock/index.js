import Mock from 'mockjs'

import article from './article'

const mocks = [].concat(article)
export function mockXHR() {
    for(let i in mocks) {
        Mock.mock(mocks[i].url, mocks[i].type || 'get', mocks[i].response)
    }
}